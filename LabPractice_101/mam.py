from operator import itemgetter
player = {}
while True:
    a = input("Input: ").split()
    b = a[0]
    if b == "done":
        break
    c = a[1]
    if c.isnumeric():
        c = int(c)
        if b in player.key():
            print("Duplicated Player")
        else:
            player[b] = c
    else:
        print("Invalid Input")
z = max(player.values())
m = sum(player.values())/len(player.keys())
if player:
    for k,v in sorted(player.items(),key = itemgetter(1),reverse = True):
        if v == z:
            print("%s\t%d\tGold"%(k,v))
        elif v < z and v > m:
            print("%s\t%d\tSilver"%(k,v))
        else:
            print("%s\t%d"%(k,v))
else:
    print("No players")