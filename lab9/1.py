def CirArea(x):
    import math as m
    x = m.pi *(m.pow(x,2))
    return(x)

def SqArea(x):
    x *= x
    return("Dasdighasdiwd",x)

a = input("Input a postitive number: ")

if a.startswith("-"):
    print("Wrong Input")
else:
    a = float(a)
    print("The are area of the circle is %.2f" %CirArea(a))
    print("The are area of the square is %d" %SqArea(a))

