l = []
jame=True
summ = 0.0
while True:
    xx = input("Numbers: ")
    try :
        xx=float(xx)
        summ += xx
    except :
        jame = False
    if jame:
        l.append("%.2f"%xx)
    if xx == "EXIT" and summ <= 1000:
        print("Exit without summary.")
        break
    if summ > 1000:
        l = sorted(l, key=float)
        print("----------")
        print(", ".join(l))
        print("sum = %.2f" %summ)
        break