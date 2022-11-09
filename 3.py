import requests
import time
from threading import Thread


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
