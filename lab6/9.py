a=[1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

c = []

for i in a:
    
    if i in b and i not in c:
        c.append(i)
    
print(c)

"""a=[1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

c = []

a = set(a)
b = set(b)

for i in a:
    for j in b:
        if i ==j or j == i:
            c.append(j)

print(c)"""