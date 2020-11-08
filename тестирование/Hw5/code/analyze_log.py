import pathlib
import pandas as pandas
from pandas.core.frame import DataFrame
from tqdm import tqdm
from mysql_clients.mysql_orm_client import MysqlOrmConnection
from tests.orm_builder import MysqlOrmBuilder


def count_req(df, req_name):
    num_req = len(df[df['REQ'].str.startswith(req_name)])
    return num_req


def sorted_dataframe(df, field_to_sort):
    return df.sort_values(field_to_sort, ascending=False)


def filter_by_code(df, from_code, to_code):
    return df[(df['STATUS_CODE'] >= from_code) & (df['STATUS_CODE'] < to_code)]


if __name__ == "__main__":
    curr_dir = pathlib.Path(__file__).parent
    logs_file = curr_dir / 'files/access.log'
    username = 'root'
    password = '123'
    dbname = 'logs'
    mysql_for_logs = MysqlOrmConnection(username, password, dbname)
    builder = MysqlOrmBuilder(mysql_for_logs)

    df = pandas.read_csv(logs_file, sep=' ', header=None,
                         names=['IP', '1', '2', 'TIME', 'UTC', 'REQ', 'STATUS_CODE', 'BYTE_SIZE', '3', 'USER_AGENT',
                                '4'])
    # количество запросов
    get_req = count_req(df, "GET")
    builder.add_CountOfReq('GET', get_req)
    post_req = count_req(df, "POST")
    builder.add_CountOfReq('POST', post_req)
    head_req = count_req(df, "HEAD")
    builder.add_CountOfReq('HEAD', head_req)
    put_req = count_req(df, "PUT")
    builder.add_CountOfReq('PUT', put_req)
    all_req = get_req + post_req + head_req + put_req
    builder.add_CountOfReq('ALL', all_req)

    # 10 самых больших по размеру запросов
    dfr = df[df['BYTE_SIZE'] != '-']
    convert_dict = {'IP': str, 'REQ': str, 'STATUS_CODE': int, 'BYTE_SIZE': int}
    dfr = dfr.astype(convert_dict)
    top_ten_sizes = sorted_dataframe(dfr, 'BYTE_SIZE').head(10)
    for row in top_ten_sizes.itertuples():
        # print(getattr(row, "IP"), getattr(row, "REQ"))
        builder.add_TopTenSizes(getattr(row, "IP"), getattr(row, "REQ"), getattr(row, "STATUS_CODE"),
                                          getattr(row, "BYTE_SIZE"))

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
    for row in top_freq_err_req.itertuples():
        # print(getattr(row, "FREQ"), getattr(row, "REQ"), getattr(row, "STATUS_CODE"))
        builder.add_TopFreqUserError(getattr(row, "FREQ"), getattr(row, "REQ"), getattr(row, "STATUS_CODE"))

    # Самые большие запросы по размеру с серверной ошибкой
    serv_err = filter_by_code(dfr, 500, 600)
    serv_err_by_size = sorted_dataframe(serv_err, "BYTE_SIZE").head(10)
    for row in serv_err_by_size.itertuples():
        # print(getattr(row, "IP"), getattr(row, "REQ"), getattr(row, "STATUS_CODE"), getattr(row, "BYTE_SIZE"))
        builder.add_TopSizesWithServError(getattr(row, "IP"), getattr(row, "REQ"), getattr(row, "STATUS_CODE"),
                                getattr(row, "BYTE_SIZE"))
