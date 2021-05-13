#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fileencoding=utf-8

from pytube import YouTube

#Получаем ссылку на видео
link = input("Вставьте ссылку на видео:  ")
yt = YouTube(link)

#Выводим информацию о видео
print("Название: ",yt.title)
print("Просмотры: ",yt.views)
print("Продолжительность: ",yt.length, "сек\n")


#Выбираем поток с максимальным разрешением
ys = yt.streams.get_highest_resolution()

print("Название: ",ys.url)
# #Загрузка
# print("Видео загружается...")
# ys.download('z:/flm/!!!GDZ/YOUTUBE/')
# print("Загрузка завершена")