"""
Выводит реальное время
Запускает таймер обратного отсчета
"""
import time
tym = time.localtime()
opt = time.strftime("%d/%m/%Y, %H:%M:%S", tym)
print(opt)


def countdown(t):
    while t > 0:
        print(t)
        t -= 1
        time.sleep(1)

print("Сколько секунд отсчитывать? Введите целое число:")
seconds = input()
seconds = int(seconds)
countdown(seconds)
