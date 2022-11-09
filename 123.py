
import requests
import time
from threading import Thread


def go_bullet(number):
    time.sleep(1)
    print(f'bullet № {number} Shoot!')


t1 = time.time()
for i in range(5):
    go_bullet(i + 1)

    print("Время на выстрел:", round(time.time() - t1, 2), "секунд")

t2 = time.time()

threads = [Thread(target=go_bullet, args=(i + 1, )) for i in range(5)]

for t in threads:
    t.start()

for t in threads:
    t.join()

print("Время на выстрел:", round(time.time() - t2, 2), "секунд")


def get_html(url):
    text = requests.get(url).text
    print(f'{url} text length is {len(text)}')


urls = ['https://pythonru.com/', 'https://www.google.com/',
        'https://github.com/', 'https://brunoyam.com/', 'https://yandex.ru/']
threads = [Thread(target=get_html, args=(urls[i], )) for i in range(5)]
t1 = time.time()
for k in threads:
    k.start()
    k.join()
print(f'Время последовательного выполнения: {time.time()-t1}\n')

threads = [Thread(target=get_html, args=(urls[i], )) for i in range(5)]
t1 = time.time()
for k in threads:
    k.start()
for k in threads:
    k.join()
print(f'Время параллельного выполнения: {time.time()-t1}')
