import datetime
import requests
import time
from bs4 import BeautifulSoup
from matplotlib import pyplot

time.sleep(2)
page = requests.get('https://mfd.ru/currency/?currency=USD')
soup = BeautifulSoup(page.text, 'lxml')
exchange_rate_styl = soup.find(
    'table', {'class': 'mfd-table mfd-currency-table'})
rs = exchange_rate_styl.find_all('tr')
a = []
b = []


for iz, row in enumerate(rs):
    if iz == 0:
        continue
    cells = row.find_all("td")
    print(f"{cells[0].text} {cells[1].text} {cells[2].text}")
    dateStr = cells[0].text.replace("с ", "")

    date = datetime.datetime.strptime(dateStr, '%d.%m.%Y').date()
    a.append(date)
    b.append(float(cells[1].text))


b.reverse()
a.reverse()
pyplot.plot(a, b)
pyplot.show()
