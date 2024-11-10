t =True
o = []
e = []

while t:
    x = int(input("Enter an integer (0 to exit): "))
    if x == 0:
        t = False
    else:
        if x % 2 == 0:
            e.append(x)
        elif x % 2 == 1:
            o.append(x)

print("-"*25)
print("The number of even integers is %d" %(len(e)))
print("The number of odd integers is %d" %(len(o)))
