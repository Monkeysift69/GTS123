x = input("Please enter your information: ").split(',')

name = ""
age = 0
t = True
if len(x) != 2:
       print("Please enter comp info")

else:
    for i in x:
        if i.isalpha():
                name = i
                
        elif i.isnumeric():
            age = int(i)
            if age <0 or age > 120:
                 t = False
                 print("Please enter comp info")
        
        else:
             t = False
             break

    if name and age and t:
         print("Your name %s" %name)
         print("Your age %d"%age)
        
    else:
         print("Please enter comp info")