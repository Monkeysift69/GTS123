x = input("Input sequence 1: ").split()
y = input("Input sequence 2: ").split()

d1 = {}
d2 = {}

for i in x:
    if i.isnumeric():
        d1[i] = True  

for j in y:
    if j.isnumeric():
        d2[j] = True


t = False
for key in d1:
    if key in d2:
        t = True
        break


if t:
    print("Output: True")
else:
    print("Output: False")