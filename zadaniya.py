import json

with open('info.json', 'w') as my_file:
    db = [
        {'name': 'hello','password': '12345678'},
        {'name': 'test123', 'password': 'helloworld'}
    ]
    json.dump(db, my_file)
def in_database(name):
    with open('info.json') as my_file:
        info_str = json.load(my_file)
        for user in info_str:
            if user['name'] == name:
                return True
        return False

def valitade_password(password):
    if len(password) < 8:
        raise Exception('Слишком короткий пороль!')
    return True

def register(name,password):
    if in_database(name):
        raise Exception('User с таким именем существует')
    if valitade_password(password):
        user = {'name': name, 'password': password}
    with open('info.json') as my_file:
        info_str = json.load(my_file)
        info_str.append(user)
    with open('info.json', 'w') as my_file:
        json.dump(info_str, my_file)
    return 'Вы успешно зарегестрировались'

register('Malik', '1234412374')
register('Salik', '32482739')

def login(name,password):
    with open('info.json') as my_file:
        info_str = json.load(my_file)
        for user in info_str:
            if user['name'] == name:
                if user['password'] == password:
                    return 'Вы успешно залогинились'
        else:
            return 'Не верные данные'

login('Salik', '32482739')

def apdate(name, old_password, new_password):
    with open('info.json') as my_file:
        info_str = json.load(my_file)
    for user in info_str:
        if user['name'] == name:
            if user['password'] == old_password:
                user['password'] = new_password
                info_str.append(user)
    with open('info.json', 'w') as my_file:
        json.dump(info_str, my_file)

apdate('Malik', '1234412374', '123456789')