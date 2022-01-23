import time
from threading import Thread
from datetime import datetime


def wait(msg):
    time.sleep(1)
    print(f"Сообщение {msg}")


choose = int(input("Введите число 1 - для последовательного запуска или число 2 - для параллельного запуска: "))
if choose == 1:
    t1 = datetime.now()

    for i in range(5):
        wait(i + 1)

    print("Время последовательного запуска:", (datetime.now() - t1).seconds)

else:
    t2 = datetime.now()
    threads = [Thread(target=wait, args=(i + 1,)) for i in range(5)]

    for t in threads:
        t.start()

    for t in threads:
        t.join()

    print("Время параллельного запуска:", (datetime.now() - t2).seconds)
