# Кортежи
import sys # import для импорта модуля sys в котором есть функция getsizeof() позволяющая узнать размер объекта

some_list = ['hello', True, 'word', 1, 2.2]
print(type(some_list), sys.getsizeof(some_list), some_list)

some_truple = ('hello', True, 'word', 1, 2.2)
print(type(some_truple), sys.getsizeof(some_truple), some_truple)
# print(dir(some_truple))

from copy import deepcopy
a = [['hello'], 10]
b = deepcopy(a)
print(id(a[0]), id(b[0]))
b[1] = 15
print(a, b)
print(id(a), id(b))
