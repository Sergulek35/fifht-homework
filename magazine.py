from my_functions import separator, refill_check


def shop():
    check = 0
    spent = 0
    story = {}
    yes = ['да', 'Да', 'ДА']
    no = ['нет', 'Нет', 'НЕТ']

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
            check = refill_check(check)
        elif choice == '2':
            while True:
                buy = int(input('Введите сумму покупки - '))
                if check >= buy:
                    buy_name = input('Введите название покупки: ')
                    check -= buy
                    story[buy_name] = buy
                    spent += buy
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
                        check = refill_check(check)
                        print('Счёт пополнен! Продолжаем')
                        print(separator(','))
                    else:
                        print(separator('*'))
                        print('Вы в главном меню!')
                        break

        elif choice == '3':
            print(separator('~'))
            print(f'Потрачено: {spent}')
            print(f'Всего покупок - {len(story)}')
            numbering = 0
            for key, value in story.items():
                numbering += 1
                print(f'{numbering}) {key} ... {value}')

        elif choice == '4':
            print(separator('^'))
            print('Вы вышли!')
            break
        else:
            print('Неверный пункт меню')
