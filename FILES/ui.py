

def input_surname():
    return input('Введите фамилию: ').title()       # начинает с загланой буквы любое введенное слово

def input_name():
    return input('Введите имя: ').title()

def input_patronymic():
    return input('Введите отчество: ').title()

def input_phone():
    return input('Введите телефон: ')

def input_address():
    return input('Введите город: ').title()

#from create_list import input_surname, input_name, input_patronymic, input_phone, input_address

def create_contact():
    surname = input_surname()
    name = input_name()
    patronymic = input_patronymic()
    phone = input_phone()
    address = input_address()
    return f'{surname} {name} {patronymic} {phone}\n{address}\n\n'

#from create_contact import create_contact

def add_contact():
    contact = create_contact()
    with open('phone_book.txt', 'a', encoding='utf-8') as file:
        file.write(contact)
        #file.flush()                                             #используется для принудительного сброса буферизированных данных в файл. Рекомендации жпт

def print_contacts():
    with open('phone_book.txt', 'r', encoding='utf-8') as file:
        contacts_all = file.read()
        #print(contacts_all)
    
    contacts_all_list = contacts_all.rstrip().split('\n\n')
    print()

    for n,cont in enumerate(contacts_all_list, 1):
        
        print(n, cont)

def search_contact():
    print(
            'Возможные варианты поиска:\n'
            '1. Фамилия\n'
            '2. Имя\n'
            '3. Отчество\n'
            '4. Номер телефона\n'
            '5. Адрес(город)'
            )
    var = input('Выберите вариант поиска: ')
    print()

    while var not in ('1','2','3','4', '5'):
            print('Некорректный ввод')
            var = input('Выберите вариант поиска: ')
    
    i_var = int(var) - 1

    search = input('Введите данные для поиска: ').title()
    with open('phone_book.txt', 'r', encoding='utf-8') as file:
        contacts_search = file.read()
    
    contacts_search_list = contacts_search.rstrip().split('\n\n')  # rstrip() - убрать справа пустоты ''
    
    for contact_str in contacts_search_list:
        contacts_details = contact_str.replace(':', '').split()
        if search in contacts_details[i_var]:
            print(contact_str)

#from function_phone_book import add_contact, print_contacts, search_contact

def interface():
    with open('phone_book.txt', 'a', encoding='utf-8'):
        pass
    
    var = ''
    while var != '4':
        print(
            'Возможные варианты:\n'
            '1. Добавить контакт\n'
            '2. Вывести на экран\n'
            '3. Поиск контакта\n'
            '4. Выход'
            )
        print()

        var = input('Выберите вариант действия: \n')

        while var not in ('1','2','3','4'):
            print('Некорректный ввод')
            var = input('Выберите вариант действия: \n')
        
        match var:
            case '1':
                add_contact()
            case '2':
                print_contacts()
                
            case '3':
                search_contact()
            case '4':
                print('До свидания!')
        print()

if __name__ == '__main__':

    interface()