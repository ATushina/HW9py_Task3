def run_action(action):
    search_contact() if action == 1 else add_contact()


def search_contact():
    search_str = input('Введите запрос (можно искать по фамилии и номеру телефона): ...')
    data = open_file('tel_book.txt').split('\n')
    header = data[0]
    data = data[1:len(data) - 1]
    res = list(filter(lambda el: el.find(search_str) != -1, data))
    if len(res) == 0:
        print('Нет такого контакта')
    else:
        res.insert(0, header)
        print('\n'.join(res))


def add_contact():
    new_contact = input('Введите данные контакта (формат "ФИО телефон"): ')
    new_contact += '\n'
    write_to_file(new_contact, 'tel_book.csv')
    write_to_file(new_contact, 'tel_book.txt')

def open_file(file_name):
    with open(file_name, 'r') as data:
        file_content = data.read()
    return file_content

def write_to_file(text: str, file_name: str):
    with open(file_name, 'a') as data:
        data.write(text)