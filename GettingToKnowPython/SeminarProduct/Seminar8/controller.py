import view, model

def start():
    view.greetings()
    while True:
        view.menu()
        answer = input('Введите команду: ')
        if answer == '1':
            contact_lst = model.read_file
            view.show(contact_lst) # вывод контактов
        elif answer == '2':
            model.add_contact() # добавить контакты
        elif answer == '3':
            model.search() # поиск
        elif answer == '4':
            view.bye()
            break # выход
        else:
            model.error() #ошибка если введено, что-то иное