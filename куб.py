# 2. Создать список, состоящий из кубов нечётных чисел от 0 до 1000:
# Вычислить сумму тех чисел из этого списка, сумма цифр которых делится нацело на 7.
# Например, число «19 ^ 3 = 6859» будем включать в сумму,
# так как 6 + 8 + 5 + 9 = 28 – делится нацело на 7.
# Внимание: использовать только арифметические операции!
# К каждому элементу списка добавить 17 и заново вычислить сумму
# тех чисел из этого списка, сумма цифр которых делится нацело на 7.
# Внимание: новый список не создавать!!!


#  создание списка кубов нечетных чисел от 0 до 1000
my_list = []  # создаем пустой список
counter = 0
while counter <= 1000:
    if counter % 2:  # если число не четное
        my_list.append(counter ** 3)  # добавить в список куб этого числа
    counter = counter + 1
print(my_list)


# вычисление суммы чисел, сумма цифр которых делится на 7
counter = len(my_list)  # устанавливаем счетчик на конец списка
sum_7 = 0  # сумма чисел делящихся нацело на 7
while counter > 0:
    sum_numeral = 0  # сумма цифр числа
    counter = counter - 1
    number = my_list[counter]  # число из списка
    while number != 0:  # вычисление суммы цифр числа
        numeral = number % 10
        number //= 10
        sum_numeral = sum_numeral + numeral
    if sum_numeral % 7 == 0:
        sum_7 = sum_7 + sum_numeral
print(sum_7)


# доабавление к каждому элементу списка 17
counter = len(my_list)  # устанавливаем счетчик на конец списка
while counter > 0:
    counter = counter - 1
    my_list[counter] = my_list[counter] + 17
print(my_list)


# вычисление суммы чисел, сумма цифр которых делится на 7
counter = len(my_list)  # устанавливаем счетчик на конец списка
sum_7 = 0  # сумма чисел делящихся нацело на 7
while counter > 0:
    sum_numeral = 0  # сумма цифр числа
    counter = counter - 1
    number = my_list[counter]  # число из списка
    while number != 0:  # вычисление суммы цифр числа
        numeral = number % 10
        number //= 10
        sum_numeral = sum_numeral + numeral
    if sum_numeral % 7 == 0:
        sum_7 = sum_7 + sum_numeral
print(sum_7)

