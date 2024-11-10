x = input("")
a = int(input("size"))
b = int(input("pattern 1 or 2"))

for i in range(a):
    for j in range(a):
        if b == 1:
            if i == j:
                print("%s"%x,end="")
            else:
                print(".", end="")
        elif b == 2:
            if j == a-i-1:
                print("%s"%x, end="")
            else:
                print(".", end="")
    print()