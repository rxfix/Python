print('Hello world')
argc = 1489
s = 0
while argc != 0:
    cout = argc % 10
    argc //= 10
    s = s + cout
    print(cout, ',', s)