user_3 = {
   'first_name': 'Иван',
   'last_name': 'Иванов',
   'patronymic': 'Иванович',
   'age': 5
}

print(user_3['first_name'])  # Иванов
print(user_3['age'])


def user_info_adv(user):
   print(f"{user['last_name']} {user['first_name']}, {user['age']:02d} лет")


user_info_adv(user_3)

user_4 = {  ######## имитация списка при помощи словаря
   0: 'Иванов',
   1: 'Иван',
   2: 'Иванович',
   3: 25
}
print(user_4[0])