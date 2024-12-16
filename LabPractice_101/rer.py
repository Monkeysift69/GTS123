from operator import itemgetter
a = {}

while True:
    x = input("Input: ").split()
    n = x[0]
    if n == "done":
        break
    m = x[1]
    m = int(m)
    if n in a.keys():
        a[n] += m
    else:
        a[n] = m
print("###Summary###")        
for k,v in a.items():
    print("Total Number of %s : %d"%(k,v))