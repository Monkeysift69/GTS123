x=  input("")

for i in x:
    if i.isnumeric():
        d = int(i)
        for j in range(d):
            if j % 3 == 2:
                print("#", end="")
            else:
                print("*", end="")
    print()