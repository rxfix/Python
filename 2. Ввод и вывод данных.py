name = 'Кеша'
age = 2
print(name, age)
print(name, age, sep='/') # Разделитель

#Перенос строки (по умолчанию \n

print(name, end=';')
print(age)

print('----------->')

#Ввод данных
name = input('Как тебя зовут:') # результатом ввода всегда будет строка
print('Привет', name)
print(type(name))
