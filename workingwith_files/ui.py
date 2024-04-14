from logger import input_data, print_data

def Interface():
    print('Добрый день, Вы попали на специальный бот-справочник от GeekBrains \n 1 - запись данных \n 2 - вывод данных \n 3 - выход')
    command = int(input('Введите вариант '))

    while command != 1 and command != 2 and command != 3:
        print('Неправильный ввод')
        command = int(input('введите вариант '))
    
    if command == 1:
        input_data()
    elif command == 2:
        print_data()
    elif command == 3:
        print('Всего доброго!')
        return


    