__author__ = 'Нестеренко Александр Валерьевич'
# Задача-1. Реализовать вывод информации о промежутке времени в
# зависимости от его продолжительности duration в секундах:
# до минуты: <s> сек;
# * до часа: <m> мин <s> сек;
# * до суток: <h> час <m> мин <s> сек;
# * *до месяца, до года, больше года: по аналогии.

duration = input('Введите продолжительность времени в секундах:')
time = int(duration)
time_list = []

if (time - 86400) >= 0:
    time_list.append(time // 86400)  # количество дней
    time = (time - (time // 86400) * 86400)  # оставшееся время

if (time - 3600) >= 0:
    time_list.append(time // 3600)  # количество часов
    time = (time - (time // 3600) * 3600)  # оставшееся время
else:
    time_list.append(0)

if (time - 60) >= 0:
    time_list.append(time // 60)  # количество минут
    time = (time - (time // 60) * 60)  # оставшееся время
else:
    time_list.append(0)

if time >= 0:
    time_list.append(time)  # количество секунд

name_list = ['сек', 'мин', 'час', 'дн']  # список врем. промежутков
time_list.reverse()

for time_inx in range(0, len(time_list)):  # дописываем к значениям промежутков их продолжительнсть
    time_list [time_inx] = str(time_list[time_inx]) + ' ' + name_list[time_inx]

time_list.reverse()

for time_inx in range(0, len(time_list)):
    print(time_list[time_inx], end=' ')


