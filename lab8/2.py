x = input("Input: ").split()

d = {}

for i in x:
    if i.isnumeric():
        i = int(i)
        if i in d:
            d[i] += 1
        else:
            d[i] = 1
    else:
        continue

for v,k in d.items():
    if k == v:
        print("Output: good sequence")
        break
    else:
        print("Output: not good sequence")
        break
