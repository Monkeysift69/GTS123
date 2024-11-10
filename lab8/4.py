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
        if ids not in d:
            d[ids] = sc
        else:
            print("Duplicated ID")

for v,k in d.items():
    print(v,k)