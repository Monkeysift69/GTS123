# highest = gold, siler < mean, else
from operator import itemgetter
d = {}

while True:
    x = input("Input: ").split()
    name = x[0]

    if name == "done":
        break

    if x[1].isnumeric():
        score = int(x[1])
        if name in d.keys():
            print("Duplicated player")
        else:
            d[name] = score
    else:
        print("Invalid input")

high = max(d.values())
mea = sum(d.values())/len(d.values())

if d:
    for k,v in sorted(d.items(), key= itemgetter(1), reverse=True):
        if v == high:
            print("%s\t%d\tGold" %(k,v))

        elif v < high and v > mea:
            print("%s\t%d\tSilver"%(k,v))

        else:
            print("%s\t%d"%(k,v))

else:
    print("No players")