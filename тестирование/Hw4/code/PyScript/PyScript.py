#! /usr/bin/python3.8
import json
import argparse
import pathlib
import pandas
from pandas.core.frame import DataFrame
from tqdm import tqdm


def read_flags():
    # curr_dir = pathlib.Path(__file__).parent
    # default_log_dir = curr_dir.parent / 'access.log'
    parser = argparse.ArgumentParser('LogAnalyzeScript')
    # path to output file
    parser.add_argument('-o', type=argparse.FileType(mode='w'), default='output.txt', dest='output')
    # path to log filetype
    """В строке ниже можно заменить required = True на default=default_log_dir и расскомментировать две строки в 
    начале def, чтобы можно было запускать без path """
    parser.add_argument('-p', type=argparse.FileType(mode='r'), required=True, dest='path_to_file')
    # jsonFlag (True or False)
    parser.add_argument('-j', type=bool, default=False, dest='jsonFlag')
    parsed = parser.parse_args()
    return {'path_to_file': parsed.path_to_file, 'output': parsed.output, 'jsonFlag': parsed.jsonFlag}


def count_req(df, req_name):
    num_req = len(df[df['REQ'].str.startswith(req_name)])
    return num_req


def sorted_dataframe(df, field_to_sort):
    return df.sort_values(field_to_sort, ascending=False)


def filter_by_code(df, from_code, to_code):
    return df[(df['STATUS_CODE'] >= from_code) & (df['STATUS_CODE'] < to_code)]


if __name__ == "__main__":
    logs_file = read_flags().get('path_to_file')
    output = read_flags().get('output')
    jsonFlag = read_flags().get('jsonFlag')

    df = pandas.read_csv(logs_file, sep=' ', header=None,
                         names=['IP', '1', '2', 'TIME', 'UTC', 'REQ', 'STATUS_CODE', 'BYTE_SIZE', '3', 'USER_AGENT',
                                '4'])

    # количество запросов каждого типа
    get_req = count_req(df, "GET")
    post_req = count_req(df, "POST")
    head_req = count_req(df, "HEAD")
    put_req = count_req(df, "PUT")
    all_req = get_req + post_req + head_req + put_req

    if jsonFlag:
        count_of_req = {
            "count_of_requests":
                {
                    "get": get_req,
                    "post": post_req,
                    "head": head_req,
                    "put": put_req,
                    "all": all_req
                }
        }
        with open("count_of_requests.json", "w") as write_file:
            json.dump(count_of_req, write_file)
    else:
        output.write("Количество запросов POST - " + str(post_req))
        output.write("\nКоличество запросов PUT - " + str(put_req))
        output.write("\nКоличество запросов GET - " + str(get_req))
        output.write("\nКоличество запросов HEAD - " + str(head_req))
        output.write("\nКоличество всех запросов - " + str(all_req))

    # 10 самых больших по размеру запросов
    dfr = df[df['BYTE_SIZE'] != '-']
    convert_dict = {'IP': str, 'REQ': str, 'STATUS_CODE': int, 'BYTE_SIZE': int}
    dfr = dfr.astype(convert_dict)
    top_ten_sizes = sorted_dataframe(dfr, 'BYTE_SIZE').head(10)

    if jsonFlag:
        top_ten_size_json = top_ten_sizes[['REQ', 'STATUS_CODE', 'BYTE_SIZE']].to_json(orient="records")
        with open("top_ten_sizes.json", "w") as file:
            json.dump(top_ten_size_json, file)
    else:
        output.write("\n10 самых больших по размеру запросов:\n")
        output.write(top_ten_sizes[['REQ', 'STATUS_CODE', 'BYTE_SIZE']].to_string())

    # 10 самых встречающихся запросов с ошибкой 4**
    errors = filter_by_code(dfr, 400, 500)
    unique_req_err = errors['REQ'].unique()
    help_fr = DataFrame(columns=['FREQ', 'REQ', 'STATUS_CODE'])
    for line in tqdm(unique_req_err):
        buf_fr = dfr[(dfr["REQ"] == line) & (dfr['STATUS_CODE'] >= 400) & (dfr['STATUS_CODE'] < 500)]
        length = len(buf_fr)
        code_err = buf_fr["STATUS_CODE"].iloc[0]
        help_fr.loc[len(help_fr)] = [length, line, code_err]
    top_freq_err_req = sorted_dataframe(help_fr, 'FREQ').head(10)

    if jsonFlag:
        top_freq_err_req_json = top_freq_err_req.to_json(orient="records")
        with open("top_frequent_error_req.json", "w") as file:
            json.dump(top_freq_err_req_json, file)
    else:
        output.write("\n10 самых встречающихся запросов с ошибкой c URL, количеством таких запросов и кодом ошибки:\n")
        output.write(top_freq_err_req.to_string())

    # Самые большие запросы по размеру с серверной ошибкой
    serv_err = filter_by_code(dfr, 500, 600)
    serv_err_by_size = sorted_dataframe(serv_err, "BYTE_SIZE").head(10)
    if jsonFlag:
        serv_err_by_size_json = serv_err_by_size[['REQ', 'BYTE_SIZE', 'STATUS_CODE']].to_json(orient="records")
        with open("serv_err_by_size.json", "w") as file:
            json.dump(serv_err_by_size_json, file)
    else:
        output.write("\n10 самых больших по размеру запросов с серверной ошибкой:")
        output.write(serv_err_by_size[['REQ', 'BYTE_SIZE', 'STATUS_CODE']].to_string())
