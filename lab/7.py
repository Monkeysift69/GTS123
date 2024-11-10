a,b,c = input("").split('*')
choice = int(input("Choice"))

a = int(a)
b= int(b)
c = int(c)

if choice == 1:
    total = a + ((b**2)+(c**3))**0.5
    print("%.2f" %total)

    total = (a*b) % c
    print("%.2f" %total)