p = 100

while True:
    x = input("Input: ").split()
    name = x[0]
    qnt = x[1]
    if name == "done" and qnt == "0":
        break
    if qnt.isnumeric():
        qnt = int(qnt)
        
        if name == 'P':
            earn = qnt // 50
            p += earn
            print("You earned %d points" % earn)
            print("Your accumulated points = %d" % p)
        
        elif name == 'R':
            if p < qnt:
                print("Not enough points")
            else:
                p -= qnt
                print("You redeemed %d points" % qnt)
                print("Your accumulated points = %d" % p)
    else:
        print("Invalid command")