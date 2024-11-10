def UserInput():
    global w,h
    w = float(input("Input your weight (kilogram: "))
    h = float(input("Input your height (meter): "))
    return w,h

def FindBMI(hh,ww):
    UserBMI = ww/(hh**2)
    return UserBMI

def ShowBMI(MyBMI):
    print("The user BMI is %.2f" %MyBMI)

UserInput()
x = FindBMI(h,w)
ShowBMI(x)