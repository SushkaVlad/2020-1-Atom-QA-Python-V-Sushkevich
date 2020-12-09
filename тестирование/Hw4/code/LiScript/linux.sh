#!/bin/bash
FILE=$1
if [ -f $FILE ]
then
path_to_file=$FILE
elif [ ! -f $FILE ] 
then 
echo "Переданного файла не существует" 
exit 1
fi
if [ -z "" ]
then
path_to_file=$(ls *.log)
fi
echo "Количество запросов:" >result && grep -E  '"POST|"GET|"PUT|"HEAD' $path_to_file |wc -l >> result && echo "ok" || echo "fail"
echo "Количество запросов POST в файле:" >>result && grep '"POST' $path_to_file |wc -l >> result && echo "ok" || echo "fail"
echo "Количество запросов PUT в файле:" >>result && grep '"PUT' $path_to_file |wc -l >> result && echo "ok" || echo "fail"
echo "Количество запросов GET в файле:" >>result && grep '"GET' $path_to_file |wc -l >> result && echo "ok" || echo "fail"
echo "Количество запросов HEAD в файле:" >>result && grep '"HEAD' $path_to_file |wc -l >> result && echo "ok" || echo "fail"
echo "Самые большие по размеру запросы с их URL, кодом, размером:">>result && sort -r -nk10 $path_to_file| awk '{print $7,$9,$10}' | head -10  >> result && echo "ok" || echo 'fail'
echo "Топ 10 запросов по количеству, которые завершились клиентской ошибкой c их количеством, URl и статус-кодом:">>result && awk '$9 ~ /^40[0-9]$/ {print $7,$9}' $path_to_file| sort -k7 -k9 | uniq -c | sort -rnk1 | head -10 >> result && echo "ok" || echo 'fail'
echo "Топ 10 запросов серверных ошибок c их URl и статус-кодом:">>result && awk '$9 ~ /50[0-9]/ {print $0}' $path_to_file | sort -nrk 10 | awk '{ print $7, $9}' | head -10 >> result && echo "ok" || echo "fail"
