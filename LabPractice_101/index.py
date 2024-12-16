from operator import itemgetter
 # {"1234": , "2222":45} {1,2 ,3 ,4}
def main():
    global a
    a = {}
    while True:
        x,y = input("Enter student ID and score: ").split()
        if x == "done" and y == "0":
            break
        if y.isnumeric():
            y = int(y)
            if y < 101:
                if x in a.keys():
                    print("The ID is already recorded!")    
                else:
                    if x.isnumeric() and len(x) == 4:
                        a[x] = y
                    else:
                        print("Invalid ID format!")
            else:
                print("Invalid score!")
        else:
            print("Invalid score!")
def m():
    print("List:  ")

main()
m()

if a:
    for k,v in sorted(a.items(),key = itemgetter(0)):
        print("%s %d"%(k,v))
else:
    print("> no score is recorded!")