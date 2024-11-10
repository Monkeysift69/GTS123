xList = []
def UserInput():
    while True:
        global t
        t= True
        x = input("Enter an input: ")
        if x == "Done":
            break
        else:
            try:
                x = int(x)
                if x < 0:
                    print("Error")
                    t= False
                    break
                else:
                    xList.append(x)

            except:
                print("Error")
                t=False
                break
    return xList      
def SumOut(xList):
    return sum(xList)
def MinOut(xList):
    return min(xList)
def MaxOut(xList):
    return max(xList)
UserInput()
if t:
    print("The summation is %d" %SumOut(xList))
    print("The summation is %d" %MinOut(xList))
    print("The summation is %d" %MaxOut(xList))