import math

months = ['январь', 'февраль', 'март', 'апрель', 'май', 'июнь', 'июль', 'август', 'сентябрь', 'октябрь',
          'ноябрь', 'декабрь']


# проверка функции filter
def filter_month(x):
    if x.startswith('я'):
        return True
    else:
        return False


def test_filter_month():
    # проверил так
    assert filter_month('я') == True
    assert list(filter(filter_month, months)) == ['январь']
    # попробовал ещё так
    result = []
    for moth in months:
        if moth.startswith('я'):
            result.append(moth)
    assert result == list(filter(filter_month, months))


# функция map

# def f_map(y):
#     return y.upper()


def test_map():
    result = []
    for month in months:
        result.append(month.upper())
    assert result == list(map(lambda y: y.upper(), months))


# функция sorted
def test_sorted():
    result = []
    for month in months:
        result.append(month)
        result.sort()
    assert result == sorted(months)


# функции из библиотеки math

# - pi -
def test_math_pi():
    assert math.pi == 3.141592653589793


# - sqrt -
def test_math_sqrt():
    assert math.sqrt(49) == 7.0
    assert math.sqrt(25) == 5.0


# - pow -
def test_math_pow():
    assert math.pow(3, 2) == 9
    assert math.pow(2, 3) == 8


#  - hypot -
def test_math_hypot():
    assert math.hypot(3, 4) == 5.0
    assert math.hypot(9, 12) == 15.0
    assert math.hypot(6, 8) == 10.0
