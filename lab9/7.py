
def myRange(FirstVal, UpperBound, StepSize):
    l = []
    for i in range(FirstVal,UpperBound,StepSize):
        l.append(i)
    return l
x = int(input("Enter the first number: "))
y = int(input("Enter upper bound: "))
z = int(input("Enter the step: "))

print("Range =",myRange(x,y,z))
