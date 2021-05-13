def url_parse(url):
    """Parses url address in tuple of items"""
    _t_protocol, _, domain, *resource_address = url.strip('/').split('/')
    t_protocol = _t_protocol[:-1]
    return t_protocol, domain, resource_address


nums = ['1578.4', '892.4', '354.1', '871.5']
print(sum(map(float, nums)))  # 3696.4  ###### именно float а не float()

urls = ['https://geekbrains.ru/teacher/lessons/7961',
        'https://www.citilink.ru/catalog/mobile/notebooks/1202859/',
        'https://www.dns-shop.ru/catalog/17a89aab16404e77/videokarty/']
urls_parsed = map(url_parse, urls)  #############  так и здесь именно url_parse а не url_parse()
print(urls_parsed)
print(*urls_parsed, sep='\n')


def total(initial, *numbers, **keywords):
    count = initial
    for number in numbers:
        count += number
    for key in keywords:
        count += keywords[key]
    return count


print(total(10, 1, 2, 4, vegetables=50, fruits=100))


def total ( initial = 5 , * numbers , extra_number ):
    count = initial
    for number in numbers :
        count += number
    count += extra_number
    print ( count )


total ( 10 , 1 , 2 , 3 , extra_number = 50 )
# total ( 10 , 1 , 2 , 3 ) # Вызовет ошибку, поскольку
