x = input("Input sequence 1: ").split()
y = input("Input sequence 2: ").split()

l1 = []
l2 = []

for i in x:
    if i.isnumeric():
        l1.append(i)

for j in y:
    if j.isnumeric():
        l2.append(j)

l1 = set(l1)
l2 = set(l2)

if l1 == l2:
    print("Output: same set")
else:
    print("Output: Different set")
