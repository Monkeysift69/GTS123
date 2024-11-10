x = input("Input: ").split()
d = {}

for i in x:
    i = i.lower()
    if i in d:
        d[i] += 1
    else:
        d[i] = 1

ma = max(d.values())

for v,k in d.items():
    if k == ma:
        print(v,"=",k)
