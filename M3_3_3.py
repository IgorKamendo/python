def best():
    stroka = input("Введите последовательность чисел через пробел: ")
    massiv = stroka.split()

    massiv.sort(reverse=True)

    print("".join(massiv))


best()
