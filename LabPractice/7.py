names = []
sublss =[]
grades = []
from operator import itemgetter
subjs = {'ce' : 0, 
         'che': 0, 
         'ec' : 0, 
         'ie':0, 
         'me':0}

while True:
    x = input("Input: ").split()
    name = x[0]
    

    if name == "done":
        break
    subj = x[1]
    grade = float(x[2])
    if grade >= 0 and grade <= 4 and subj in subjs:
        if subj == 'ce':
            subjs['ce'] += 1
        elif subj == 'che':
            subjs['che'] += 1
        elif subj == 'ec':
            subjs['ec'] += 1
        elif subj == 'ie':
            subjs['ie'] += 1
        elif subj == 'me':
            subjs['me'] += 1
        names.append(name)
        sublss.append(subj)
        grades.append(grade)
        
    else:
        print("Error")

print("----summary----")
for k,v in subjs.items():
    print("%s = %d" % (k,v))
print("----LIST----")
if names and sublss and grades:
    #   0  1  2
    for i, j, k in sorted(zip(names, sublss, grades), key = itemgetter(2), reverse=True):
        print("%s\t%s\t%.2f" % (i, j, k))
else:
    print("The list is empty")