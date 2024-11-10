import math as m

a, b = input("").split()
a = int(a)
b = int(b)

if a > b:
    smaller = b
    greater = a
elif a < b:
    smaller = a
    greater = b
total = 0

for i in range(1, greater+1):
    total = sum(range(smaller, greater+1))

s = m.sqrt(total)

print("Min %d" %smaller)
print("Max %d" %greater)
print("= %.2f" %s)