from operator import itemgetter
depart = {"ce":0,
    "che":0,
    "ec":0,
    "ie":0,
    "me":0}
name_grade = {}

while True:
    x = input("Input: ").split()
    name = x[0]

    if name == "done":
        break

    department  = x[1]
    grade = x[2]
    
    grade = float(grade)
    if grade >= 0.00 and grade <= 4.00: 
        if department in depart.keys():
            depart[department] += 1
            name_grade[name] = (department,grade) # name_grade[name] =grade
        else:
            print("ERROR")
    else:
        print("ERROR")

print("----SUMMARY----")
for k,v in depart.items():
    print("%s = %d" %(k,v))

"""print("ce = %d" %depart["ce"])
print("che = %d" %depart["che"])
print("ec = %d" %depart["ec"])
print("ie = %d" %depart["ie"])
print("me = %d" %depart["me"])"""


for i,(j,k) in sorted(name_grade.items(), key = itemgetter(1)): #a[1]
    print("%s %s %.2f" %(i,j,k))