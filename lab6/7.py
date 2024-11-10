import random as r
list1 = []


for i in range(4):
    ra = r.randint(1,4)
    i+=1
    x = input("Enter string#%d: "  %i)
    list1.append(x)

r.shuffle(list1)

print("Random order of sentence:", " ".join(list1))