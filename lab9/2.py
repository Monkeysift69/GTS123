def Right_Rotate(x,n):
    return x[-n:] + x[:-n]
def Left_Rotate(x,n):
    return x[n:] + x[:n]

x = input("Enter 5 inputs: ").split()

try:
    n = int(input("Enter an integer number of rotations (0-4): "))
    if len(x) > 5:
        print("Error!")
    else:
        if n >= 1 and n <= 4:
            print("The left-rotated list: %s" %Left_Rotate(x,n))
            print("The Right-rotated list: %s " %Right_Rotate(x,n))
        else:
            print("Error!")
except:
    print("Error!")