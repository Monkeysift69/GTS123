d = {}

while True:
    idinp = input("Enter stdent ID and score: ").split()
    ids = idinp[0]
    score = idinp[1]
    if ids == "done" and score == '0':
        break
    else:
        if len(ids) == 4:
            if ids.isnumeric():
                ids = int(ids)
                if score.isnumeric():
                    score = int(score)
                    if score <= 100 and score >= 0:
                        
                        if ids in d:
                            print("The ID is already recorded!")
                        else:
                            d[ids] = score
                    else:
                        print("Invid score!")
                else:
                    print("Invalid score!")
            else:
                print("Invalid ID format!")
        else:
            print("Invalid ID format!")

c = len(d.keys())

def avg():
    try:
        l = []
        for i in d.values():
            l.append(i)
        avge = sum(l)/c
        return avge
    except:
        pass

print("List: ")

if d:
    for k,v in sorted(d.items()):
        print("%s %s" %(k,v))
    print("There are %d student(s). the average score is %.2f points" %(c, avg()))

else:
    print("> no score is recorded")