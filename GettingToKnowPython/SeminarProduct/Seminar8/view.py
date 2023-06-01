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

def show(contact_lst: list):
    for contact in contact_lst:
        print(contact)
