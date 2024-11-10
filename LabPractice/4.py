names = []
score = []
from operator import itemgetter

while True:
    x = input("Input: ").split()
    
    name = x[0]

    if len(x) == 1 and x[0] == 'done':
        break
    
    if len(x) != 2:
        continue
    qnt = x[1]
    if qnt.isnumeric() and int(qnt) > 0:
        qnt = int(qnt)
        if name in names:
            print("Duplicate player")
        else:
            names.append(name)
            score.append(qnt)
    else:
        print("Invalid input")


medal = ['Gold', 'Silver']

if names and score: 
    avg = sum(score) / len(score)
    for i, j in sorted(zip(names, score), key= itemgetter(1) , reverse=True):
        ma = max(score)
        if j == ma:
            print("%s\t%d\t%s" % (i, j, medal[0]))
        elif j >= avg and j < ma:
            print("%s\t%d\t%s" % (i, j, medal[1]))
    print("Average score = %.2f" % avg)