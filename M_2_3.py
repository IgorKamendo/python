x = input("Введите пароль из 8 символов, который включает прописные и заглавные буквы ")

while not len(x) == 8 or x.isupper() or x.islower():
    print("Error, try again")
    x = input("Введите пароль из 8 символов, который включает прописные и заглавные буквы ")
else:
    print("OK")
