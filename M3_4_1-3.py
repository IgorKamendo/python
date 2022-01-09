import json


# data = {"login": "passwrd"}
# with open("register.json", "w") as f:
#   json.dump(data, f)


def register(login, passwrd):
    with open("register.json", "r") as f:
        data = json.load(f)
    if login not in data.keys():
        data[login] = passwrd
        with open("register.json", "w") as f:
            json.dump(data, f)


def login_function(login, passwrd):
    with open("register.json", "r") as f:
        data = json.load(f)
    if login in data.keys():
        print("Данный логин уже существует")
    else:
        print("Ок")


while True:
    break_point = input("Стоп? ")
    if break_point == "да":
        break
    q = input("Добавить или проверить? ")
    if q == "добавить":
        login = input("Введите логин ")
        passwrd = input("Введите пароль ")
        register(login, passwrd)
    elif q == "проверить":
        login = input("Введите логин ")
        passwrd = input("Введите пароль ")
        login_function(login, passwrd)
