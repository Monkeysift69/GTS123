l = [] 
t = True
summ = 0.0 
while True:
    x = input("Numbers: ")
    try:
        x=float(x)
        summ += x
        t = True
    except ValueError:
        t = False
    if t:
        l.append("%.2f"%x)
    if x == 'EXIT' and summ <= 1000:
        print("Exit without summary.")
        break

    if summ > 1000:
        l = sorted(l, key=float)
        print("----------")
        print(", ".join(l))
        print("sum = %.2f" %summ)
        break