
from bs4 import BeautifulSoup
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
