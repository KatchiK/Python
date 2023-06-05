def greetings():
    print("Приветствуем Вас в телефонном справочнике!")

def menu():
    print('Выберите действие:\n'
          '1 - Вывод списка контактов\n'
          '2 - Добавить контакт\n'
          '3 - Поиск\n'
          '4 - Выход\n'
          )
    #pass 

def show(contact_lst):
    
    for contact in contact_lst:
        print(contact)
    
def input_data():
    return input("Введите Имя")

def show_search(contact):
        print(contact)

def search_input():
    return input("Введите поисковый запрос")

def bye():
    print("Благодарим за использование программы")
    