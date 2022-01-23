from datetime import datetime
from threading import Thread
import requests


def get_html(link):

    r = requests.get(link)
    print(r.text)


links = ["http://yandex.ru", "http://mail.ru", "http://google.ru", "http://rambler.ru", "http://auto.ru"]
threads = [Thread(target=get_html, args=[links[i]]) for i in range(5)]

choose = int(input("Введите число 1 - для последовательного запуска или число 2 - для параллельного запуска: "))
if choose == 1:
    t1 = datetime.now()

    for i in range(5):
        print(get_html(links[i]))
        print("Время последовательного запуска:", (datetime.now() - t1).seconds)

else:
    t2 = datetime.now()

    for t in threads:
        t.start()

    for t in threads:
        t.join()

    print("Время параллельного запуска:", (datetime.now() - t2).seconds)
