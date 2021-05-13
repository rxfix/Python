MONEY_UNITS = 'руб'
MONEY_CENTS = 'коп'


def show_price(items):
    for price in items:
        price = int(round(price * 100))
        rubles = price // 100
        cents = price % 100
        print(f'{rubles:02d} {MONEY_UNITS} {cents:02d} {MONEY_CENTS}')


prices = [57.8, 46.51, 97, 89.99, 52.1, 45, 64.28, 4.21, 7, 42.42, 35.45, 101.01, 5.0, 75.00, 42.07]
show_price(prices)