import os
import shutil


def separator(simbol):  # Разделитель
    return simbol * 40


def refill_check(check):  # Пополнение счёта
    sum_buy = int(input('Введите сумму - '))
    check += sum_buy
    return check


def file_search(folder_files):  # Поиск файлов или папок
    for dir, folder, files in os.walk(os.getcwd()):
        if folder_files == 'папки':
            print(folder)
        elif folder_files == 'файлы':
            print(files)


def examination_folder(folder_copy_delete):  # Удаление и копирование папок
    user_input = input('Введите имя папки: ')

    if os.path.isdir(user_input):
        if folder_copy_delete == 'удалить папку':
            os.rmdir(user_input)
            print(separator(':'))
            print(f'папка {user_input} удалена')

        elif folder_copy_delete == 'копировать папку':
            shutil.copytree(user_input, input('Новое имя - '))
            print(separator(':'))
            print(f'папка {user_input} скопирована')
    else:
        print(separator('<>'))
        print('Не удаётся найти папку!')


def examination_files(files_copy_delete):  # Удаление и копирование файлов
    user_input = input('Введите имя файла: ')
    if os.path.isfile(user_input):
        if files_copy_delete == 'удалить файл':
            os.remove(user_input)
            print(separator(':'))
            print(f'файл {user_input} удалён')

        elif files_copy_delete == 'копировать файл':
            shutil.copyfile(user_input, input('Новое имя - '))
            print(separator(':'))
            print(f'файл {user_input} скопирован')
    else:
        print(separator('<>'))
        print('Не удаётся найти файл!')


def menu():  # Основное меню
    print(separator('='))
    print('1. создать папку')
    print('2. удалить папку')
    print('3. удалить файл')
    print('4. копировать папку')
    print('5. копировать файл')
    print('6. просмотр содержимого рабочей директории')
    print('7. посмотреть только папки')
    print('8. посмотреть только файлы')
    print('9. просмотр информации об операционной системе')
    print('10. создатель программы')
    print('11. играть в викторину')
    print('12. мой банковский счет')
    print('13. выход')
    print(separator('-'))
