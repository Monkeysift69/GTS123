t = True
l = []
c = 0
while True:
    x = int(input("Enter an integer (-1 to exit): "))
    if x == -1:
        break
    else:
        l.append(x)
    c+=1

print("The sum of %d number(s) is %d" %(c,sum(l)))