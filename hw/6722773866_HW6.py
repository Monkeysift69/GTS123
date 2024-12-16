import numpy as np

def dist(p1, p2):
    distance = np.sqrt(np.sum((p1-p2)**2))
    return distance

p = [] #[[x1,y1,z1],[x2,y2,z2]]
c = 0
Tr = True
while True:
    x = input("P%d: "%(c+1))
    
    if x.lower() == 'end':
        break
    try:
        l=[]
        for i in x.split():
            i = float(i)
            l.append(i)
        if len(l) == 3:
            p.append(np.array(l))
            c += 1
            
    except ValueError:
        continue
    
if len(p) <2:
    print("There are fewer than two points. There is no distance output.")
    Tr = False


if Tr:
    print("There are %d points in total." %len(p))
    d = 0
    for i in range(1, len(p)):
        dista = dist(p[i - 1], p[i])
        d += dista
        print("P%d -> P%d = %.2f" %(i,i+1,dista))

    print("Total distance is %.2f units." %d)
