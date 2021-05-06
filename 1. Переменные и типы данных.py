name = 'Кеша'
age = 2
period = 2.1
is_good = True
person = None

print(type(name))
print(type(age))
print(type(period))
print(type(is_good))
print(type(person))

#Приведение типов
birthday_year = '1988'
period = 20
age = int(birthday_year) + period
print(age)

birthday_year = '1988'
period = 20
age = birthday_year + str(period)
print(age)