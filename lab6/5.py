a = []
b = []
c = []

x = int(input("How many people in a group?"))

for i in ['A', 'B', 'C']:
    print("please enter grade from group", i)
    for j in range(x):
        grade = float(input("enter grade: "))
        if i == 'A':
            a.append(grade)
            
        elif i == 'B':
            b.append(grade)
            
        elif i == 'C':
            c.append(grade)
    print()

amax = max(a)
bmax = max(b)
cmax = max(c)

print("The highest grade of group A is ",amax)
print("The highest grade of group B is ",bmax)
print("The highest grade of group C is ",cmax)
