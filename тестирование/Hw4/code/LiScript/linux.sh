#!/bin/bash
FILE=$1
if [ -f $FILE ]
then
echo "Файл существует"
path_to_file=$FILE
elif [ ! -f $FILE ] 
then 
echo "Переданного файла не существует" 
exit 1
elif [ ! -n $FILE ]
then
path_to_file=$(ls *.log)
fi
echo "Количество запросов в файле:" >output && grep -E  "POST|GET" $path_to_file |wc -l >> output && echo "ok" || echo "fail"
echo "Количество запросов POST в файле:" >>output && grep "POST" $path_to_file |wc -l >> output && echo "ok" || echo "fail"
echo "Количество запросов GET в файле:" >>output && grep "GET" $path_to_file |wc -l >> output && echo "ok" || echo "fail"
echo "Самые большие по размеру запросы с их количеством, URL, кодом:">>output && sort -r -nk10 $path_to_file| awk '{print $7,$9}' | uniq -c | head -10  >> output && echo "ok" || echo 'fail'
echo "Топ 10 запросов по количеству, которые завершились клиентской ошибкой c их количеством, URl и статус-кодом:">>output && awk '$9 ~ /^40[0-9]$/ {print $7,$9}' $path_to_file| sort -k7 -k9 | uniq -c | sort -rnk1 | head -10 >> output && echo "ok" || echo 'fail'
echo "Топ 10 запросов серверных ошибок c их URl и статус-кодом:">>output && awk '$9 ~ /50[0-9]/ {print $0}' $path_to_file | sort -nrk 10 | awk '{ print $7, $9}' | head -10 >> output && echo "ok" || echo "fail"
