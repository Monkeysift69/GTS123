def SquareArea(x):
    a = x * x
    return a

def CircleArea(r):
    a = (22/7)*(r**2)
    return a

x = input("Do you want to find the area of a square (s) or a circle (c)?: ")
y = int(input("Enter the length: "))
if x == 's':
    print("The area of the square is %.2f"%SquareArea(y))
elif x == 'c':
    print("The area of the circle is %.2f"%CircleArea(y))
else:
    print("Wrong Input")