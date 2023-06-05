
def creating_contact(data: str):
    """file = open('file.txt', 'a', encoding='utf-8')
    file.write(data)
    file.close()"""

    with open('file.txt', 'a', encoding='utf-8' ) as file:
        file.write(f'{data}\n')

    #with open('file.txt', encoding='utf-8' ) as file:
        #content = file.read()
    #print(content)

def read_file():
   
    with open('file.txt', encoding='utf-8' ) as file:
        return file.read().split('\n')[:-1]

    """
    file = open('file.txt', 'a', encoding='utf-8')
    data = file.read().split('\n')[:-1]
    file.close()
    return data
    """
   
def search(search_query: str):
    with open('file.txt', 'r', encoding='utf-8') as file:
        for line in file:
            if search_query in line:
                return line
            
      
            



    # return ()#возвращает найденную строку 

