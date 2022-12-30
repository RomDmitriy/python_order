import requests  # для получения WEB-страницы

# pip install bs4
from bs4 import BeautifulSoup # для парса HTML страницы

# получаем WEB-страницу
response = requests.get('https://finance.rambler.ru/currencies/').text
# используем BeatifulSoup (с его помощью легче парсить HTML)
soup = BeautifulSoup(response, "html.parser")

# из всей страницы получает нужную нам часть (про доллар США):
# <a class="finance-currency-table__tr" title="Доллар США" href="/currencies/USD/" data-blocks="USD">
# <div class="finance-currency-table__cell finance-currency-table__cell--code">
# USD
# </div>
# <div class="finance-currency-table__cell finance-currency-table__cell--denomination">
# 1
# </div>
# <div class="finance-currency-table__cell finance-currency-table__cell--currency">
# Доллар США
# </div>
# <div class="finance-currency-table__cell finance-currency-table__cell--value">
# 57.9990
# </div>
# </a>
value = soup.find('a', {'data-blocks': 'USD'})

# берем div, где лежит курс:
# <div class="finance-currency-table__cell finance-currency-table__cell--value">
# 57.9990
# </div>
value = value.find('div', class_='finance-currency-table__cell--value')

# избавляемся от тегов:
# \n
# 57.9990
# \n
value = value.text

# избавляемся от лишних переходов на новую строку:
# 57.9990
value = value.replace('\n', '')

# вывод
print('Курс доллара:', value)
