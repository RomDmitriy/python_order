import socket  # для получения IP-адреса сайта
import requests  # для HTTP запросов

# pip install pythonping
from pythonping import ping  # для ping к сайту

# Часть 1
request_count = 34  # количество ping (номер варианта + 10)
url = 'www.fsb.ru'  # URL сайта
IP_address = socket.gethostbyname(url)  # получаем IP адрес сайта

print('IP:', IP_address)  # вывод IP

rtt_arr = []  # для хранения RTT

for i in range(request_count):
    # пингуем. count = 1 т.к. нам нужны значения RTT отдельно
    res = ping(IP_address, count=1)
    if res.success():  # если получилось
        rtt_arr.append(res.rtt_avg_ms)  # берем RTT

# среднее значение
rtt_avg = 0  # для хранения среднего RTT
for i in range(len(rtt_arr)):
    rtt_avg += rtt_arr[i]  # получаем сумму всех RTT
rtt_avg /= len(rtt_arr)  # получаем среднее RTT

# средне-квадратичное отклонение
rtt_deviation = 0  # для хранения средне-квадратического отклонения
# реализация формулы https://calculatorium.ru/images/math/standard-deviation.png
for i in range(len(rtt_arr)):
    rtt_deviation += pow((rtt_arr[i] - rtt_avg), 2)
rtt_deviation /= len(rtt_arr)
rtt_deviation **= 0.5

# вывод
print('Количество успешных ping:', len(rtt_arr))
print('Значения RTT:', rtt_arr)
print('Среднее значение RTT:', rtt_avg)
print('Средне-квадратичное отклонение RTT:', rtt_deviation)

# Часть 2
# делаем HTTP-запрос:
# http://ip-api.com - сайт, куда делаем запрос
# json - формат ответа сервера
# {IP_address} - IP адрес, о котором хотим получить информацию
# ?fields=regionName,zip - запрашиваем информацию о регионе и почтовом индексе IP-адреса
# json() - ответ преобразовываем в json-формат
res = requests.get(f'http://ip-api.com/json/{IP_address}?fields=regionName,zip').json()

# вывод
print('Район:', res.get('regionName'))
print('Почтовый индекс:', res.get('zip'))
