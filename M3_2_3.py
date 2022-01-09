d = {"name1": "id1", "name2": "id2", "name3": "id3"}
L = []
P = []

for i in d:
    L.append(i)
    P.append(d[i])

d2 = {}

for i in range(len(L)):
    d2[P[i]] = L[i]

print(d2)
