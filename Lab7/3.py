x = int(input("Enter a number: "))
i=0

while i < x:
    
    j = 0
    while j < x:
        if i == 0 or i == x-1 or j == 0 or j == x-1:
            print("o", end=" ")
        elif i <= j:
            print("x",end=" ")
        else:
            print(" ", end=" ")
        j+=1
    print()
    i += 1