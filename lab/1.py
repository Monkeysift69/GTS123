import math as m

choice = input("Input a shape T/S/C: ")
l = int(input("Input a length: "))

if choice == 'T':
    tri = 0.5 * l * (l/2)
    print("The surface area of triangle is %.2f" %tri)

elif choice == 'S':
    s = m.pow(l,2)/2
    print("The surface area of surface area is %.2f" %s)

elif choice == 'C':
    c = m.pi * m.pow(l/2,2)
    print("The surface area of circle is %.2f" %c)

else:
    print("Length must be more than or equal to zero")