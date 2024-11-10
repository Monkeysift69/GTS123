x = input("Input a sentece: ").lower()
x = x.split()
d = {}

for i in x:
    if i in d:
        d[i] += 1
    else:
        d[i] = 1
print("Output: ")
for k,v in d.items():
    if v > 1:
        print(k)
        t = True

if not t:
    print("none")