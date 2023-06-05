import view, model

def start():
    view.greetings()
    while True:
        view.menu()
        answer = input('Введите команду: ')
        if answer == '1':
            contact_lst = model.read_file()
            view.show(contact_lst) # вывод контактов
        elif answer == '2':
            model.creating_contact(view.input_data()) # добавить контакты
        elif answer == '3':
            view.show_search(model.search(view.search_input())) # поиск
            #model.search(()) 
        elif answer == '4':
            view.bye()
            break # выход
        else:
            model.error() #ошибка если введено, что-то иное
