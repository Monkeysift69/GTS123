import math as m

def myCylinder(r,h):
    v = m.pi*(r**2)*h
    a = (2*m.pi*r*h )+(2*m.pi*(r**2))
    return v, a

x = float(input("Enter the radius r of the cylinders: "))
y = float(input("Enter the height h of the culinders: "))

print("The volume is %.2f and the surface area is %.2f" %myCylinder(x,y))