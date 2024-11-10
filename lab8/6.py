x = ""
d = {}

while x != "DONE":
    x = input("Input (DONE = exit): ")
    
    if x != "DONE":
        ids,sc = x.split(" ")
        if not sc.isnumeric():
            print("Invalid Input")
            continue
        if not ids.isnumeric():
            print("Invalid Input")
            continue
        if ids in d:
            if sc > d[ids]: 
                d[ids] = sc
        else:
            d[ids] = sc


for v,k in d.items():
    print(v,k)