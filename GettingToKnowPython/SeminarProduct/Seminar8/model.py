def add_contact(data: str):
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


if __name__ == '__main__':
    add_contact('Hello world')