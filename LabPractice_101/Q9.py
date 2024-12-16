l={}
while True:
    i=input("Input:")
    if i == "done":
        break
    else:
        a,b=i.split()
        b=int(b)
        if a in l.keys():
            l[a] += b
        else:
            l[a] = b

print("###Summary###")

if l:
    for k,v in l.items():
        print("Total Number of %s : %d"%(k,v))

else:
    print("Empty List")