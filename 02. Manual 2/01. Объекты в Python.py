# a = 14
# print(type(a))
#
# # Проверка типа перемеенных
# winter_mouths = ['декабрь', 'январь', 'февраль']
# print(type(winter_mouths) == list)
# print(isinstance(winter_mouths, list))

# Методы объекта
# print(dir(winter_mouths))

# winter_mouths.append(12)
# print(winter_mouths)
# winter_mouths.extend([1, 2])
# print(winter_mouths)
# winter_mouths.append([1, 2])
# print(winter_mouths)
#
# cur_winther_mouths = winter_mouths.pop()
# print(winter_mouths)
# print(cur_winther_mouths)

# # basket_price = [3000.0, 1580.0, 3000.0, 2785.0]
# # print(basket_price.count(3000.0))  # считае сколько объектов есть в списке -> 2
# # print(basket_price.index(3000.0))  # узнать индекс вхождения первого объекта в список -> 0
# print(winter_mouths, id(winter_mouths))
# winter_mouths.insert(1, 'новый месяц')
# print(winter_mouths, id(winter_mouths))
#
# winter_mouths = ['декабрь', 'январь', 'январь', 'январь', 'февраль',]
# while winter_mouths.count('январь') > 1:
#     winter_mouths.remove('январь')
#     print(winter_mouths, id(winter_mouths))

# # Реверс списов
# winter_mouths = ['декабрь', 'январь', 'февраль']
# print(id(winter_mouths), winter_mouths)
# winter_mouths.reverse()
# print(id(winter_mouths), winter_mouths)
# winter_mouths_revesed = list(reversed(winter_mouths))
# print(id(winter_mouths_revesed), winter_mouths_revesed

# # Срезы на примере списков
# year_months = ['янв', 'фев', 'мар', 'апр', 'май', 'июн',
#                'июл', 'авг', 'сен', 'окт', 'ноя', 'дек']
# first_quarter = year_months[0:3]
# print(first_quarter)
# other_first_quarter = year_months[:3]
# print(other_first_quarter)
# secpond_quarter = year_months[3:6]
# print(secpond_quarter)
# last_quarter = year_months[9:]
# print(last_quarter)
# odd_months = year_months[::2]
# print(odd_months)
# even_months = year_months[4:2:-1]
# print(even_months)

# Сортировка списков
winter_months = ['декабрь', 'январь', 'февраль']
print(id(winter_months))
winter_months.sort()
print(id(winter_months))
print(winter_months, chr(128526))

winter_months = ['декабрь', 'январь', 'февраль']
print(id(winter_months))
winter_months_s = sorted(winter_months, reverse=True)
print(id(winter_months_s), type(winter_months_s))
print(winter_months_s)