import os
from lesson_5.my_functions import separator, refill_check, file_search


# https://yadi.sk/d/n6gyaovRG2JdAA --- ссылка не работает!!!

# тест своих функции

def test_separator():
    assert separator('-') == '----------------------------------------'


def test_refill_check():
    assert refill_check(0, 250) == 250
    assert refill_check(250, 150) == 400


def test_file_search():
    assert file_search('папки') in [os.getcwd(), file_search('папки')]
    assert file_search('файлы') in [os.getcwd(), file_search('файлы')]

# остальные не получилось , функции не чистые, надо переписывать
