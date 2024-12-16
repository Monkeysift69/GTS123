import operator

d ={} # {"1" : 1, "5":2}

while True:

    x = input("Enter a number: ")

    if x == "done":
        break

    else:
        if x.isnumeric(): # "-"
            x = int(x)
            if x >= 1 and x <= 1000:     
                if x in d:
                    d[x] += 1
                else:
                    d[x] = 1
            else:
                print("Error")
        else:
            print("Error")

print("----SUMMARY----")

for k,v in d.items():
    pass