d = {
    1: 0,
    2: 0,
    5: 0,
    10: 0,
}

c = 0

print("Welcome to coin deposit machine")
while True:
    x = input("Please insert coin: ")
    if x == "done":
        break
    
    x = int(x)

    if x not in d:
        print("Only 1, 2, 5, 10 coins are allowed")
        continue
    else:
        if x == 1:
            d[1] += 1
            c += 1
            print("You inserted 1 baht coin")
            print("Current balance: %d baht" % c)
        elif x == 2:
            d[2] += 1
            c += 2
            print("You inserted 2 baht coin")
            print("Current balance: %d baht" % c)
        elif x == 5:
            d[5] += 1
            c += 5
            print("You inserted 5 baht coin")
            print("Current balance: %d baht" % c)
        elif x == 10:
            d[10] += 1
            c += 10
            print("You inserted 10 baht coin")
            print("Current balance: %d baht" % c)

print("----SUMMARY----")
print("1 baht coins -> %d" % d[1])
print("2 baht coins -> %d" % d[2])
print("5 baht coins -> %d" % d[5])
print("10 baht coins -> %d" % d[10])
print("Depsite Amount: %d baht" % c)