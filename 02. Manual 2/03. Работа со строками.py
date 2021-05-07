# massage = 'привет всем'
# print(massage[:massage.index(' ')])
# print(ord(massage[0]))
# print(chr(ord(massage[0]) - 32))
# print(massage[::-1])

# raw_message = ['python', 'современный', 'язык']
# message = ''
# for item in raw_message:
#     message += item
#     message += ' '
# print(message)
#
# message = ' '.join(raw_message)
# print(message)
#
# name, year = 'Иван', 2021
# greeting = 'Уважеемый, %s! Поздравляем с %d годом!' % (name, year)
# print(greeting)
#
# greeting = 'Уважаемый, {}! Поздравляем с {} годом!' .format(name, year)
# print(greeting)
#
#
name, year, month, money = 'Борис', 2021, 3, 1789.47689
# mes = '{2}! Сегодня {1} месяц {0} года.'.format(year, month, name)
# mes_2 = '{2:15}! Сегодня {1:02d} месяц {0} года'.format(year, month, name)
# mes_3 = '{name:>15}! На счете {money:.2f}'.format(name=name, money=money)
# print(mes_2)
#
greeting = f'Уважаемый {name} ! Поздравляем с {year} годом.'
mes_2 = f'{name:^15} Сегодня {month:02d} месяц {year} года.'
mes_3 = f'{name:>15}! На счете {money:2f}'
print(mes_2)

# # .split
# url = 'https://geekbrains.ru/teacher/lessons/79615'
# url_parts = url.split('/')
# print(url_parts)
#
# _t_ptotocol, _, domain, *resource_address = url.split('/')
# t_ptotocol = _t_ptotocol[:-1]
# print(t_ptotocol, domain, resource_address)
# _t_ptotocol, _, domain, *resource_address = url.split('/')[:3]
# t_ptotocol = _t_ptotocol[:-1]
# print(t_ptotocol, domain, resource_address)
#
# msg = 'Товаров в корзине: 5'
# r = []
# r = reversed(msg)
# print(type(r))
