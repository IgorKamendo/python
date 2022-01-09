L = [1, 4, 1, 6, "hello", "a", 5, "hello"]

L_unique = []
L_repeat = []

for i in L:
    if i not in L_unique:
        L_unique.append(i)
    elif i in L_unique:
        L_repeat.append(i)

print(L_repeat)
