x = int(input("Enter an inther number: "))

if x > 10:
    print("1 - 10 !!!!")
else:
    i=1
    while i <= x:
        for j in range(1, i+1):
            print(j,end=" ")
        print()
        i+=1


    i=x-1
    while i > 0:
        for j in range(1,i+1):
            print(j,end=" ")
        print()
        i -=1