from operator import itemgetter

cur = [] # currency
am = [] # converted currency
icur = []  #initial amount

while True:
    x = input("Input: ")
    if x== 'end':
        break
    
    currency,amount = x.split()
    amount = float(amount)
    if currency == "JPY":
        cur.append(currency)
        icur.append(amount)
        am.append(amount*0.29)

    elif currency == "USD":
        cur.append(currency)
        icur.append(amount)
        am.append(amount*31.99)

    elif currency == "EUR":
        cur.append(currency)
        icur.append(amount)
        am.append(amount*35.62)
        
    else:
        print("Error")

for i,j,k in sorted(zip(icur,cur, am), key = itemgetter(2)):
    print("%.2f %s is %.2f THB" %(i,j,k))