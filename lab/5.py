a,b,c = input("").split()


a = a == 'True'
b = b == 'True'
c = c == 'True'

if not a and not b and not c: print("Grant")
elif not a and not b and c: print("Deny") 
elif not a and  b and not c: print("Deny") 
elif not a and b and c: print("Deny") 
elif a and not b and c: print("Grant") 
elif a and not b and c: print("Grant") 
elif a and b and not c: print("Grant") 
elif a and b and c: print("Grant") 