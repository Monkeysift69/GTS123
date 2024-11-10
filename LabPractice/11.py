d = {}

while True:
    x = input("Input: ").split()
    name = x[0]
    if name == "done":
        break
    if len(x) != 2:
        continue
   
    try:
        qnt = int(x[1])
        if name in d:
            d[name] += qnt
        else:
            d[name] = qnt
    except:
        break
    
for k,v in d.items():
    print("Total Number of %s : %d" %(k,v))