from my_functions import separator, refill_check
import os
import json


def shop():
    check = 0
    story = {}
    yes = ['да', 'Да', 'ДА']
    no = ['нет', 'Нет', 'НЕТ']
    if os.path.exists('check.txt'):
        with open('check.txt', 'r') as f:
            check = json.load(f)

    if os.path.exists('story.txt'):
        with open('story.txt', 'r') as f:
            story = json.load(f)

    while True:
        print(separator('/'))
        print(f'Ваш счёт: {check}')
        print('1. пополнение счета')
        print('2. покупка')
        print('3. история покупок')
        print('4. выход')
        print(separator('-'))

        choice = input('Выберите пункт меню: ')
        if choice == '1':
            try:
                sum_buy = int(input('Введите сумму - '))
                check = refill_check(check, sum_buy)
            except ValueError:
                print('Вы ввели не число!\nПереход в меню ')

        elif choice == '2':
            while True:
                try:
                    buy = int(input('Введите сумму покупки - '))
                    if check >= buy:
                        buy_name = input('Введите название покупки: ')
                        check -= buy
                        story[buy_name] = buy
                        print(separator('*'))
                        continued = input('Продолжить покупки? ')
                        if continued in yes:
                            print(separator('.'))
                        elif continued in no:
                            print('СПАСИБО ЗА ПОКУПКУ!')
                            break
                        else:
                            print(separator('*'))
                            print('Неверный ввод !\nВы в главном меню!')
                            break
                    else:
                        print('Увы, не хватает средств на счетё!')
                        print(separator(','))
                        refill = input('Хотите пополнить счёт? ')
                        if refill in yes:
                            sum_buy = int(input('Введите сумму - '))
                            check = refill_check(check, sum_buy)
                            print('Счёт пополнен! Продолжаем')
                            print(separator(','))
                        else:
                            print(separator('*'))
                            print('Вы в главном меню!')
                            break
                except ValueError:
                    print(separator('. .'))
                    print('Не правельный ввод\nнужно ввести число! ')


        elif choice == '3':
            print(separator('~'))
            print(f'      Потрачено: {sum(story.values())}')
            print(f'Всего покупок - {len(story)}')
            numbering = 0
            for key, value in story.items():
                numbering += 1
                print(f'{numbering}) {key} ... {value}')


        elif choice == '4':
            print(separator('^'))
            print('Вы вышли!')
            with open('check.txt', 'w') as f:
                json.dump(check, f)

            with open('story.txt', 'w') as f:
                json.dump(story, f)
            break
        else:
            print('Неверный пункт меню')
