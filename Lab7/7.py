p,t,c=0,0,0
while p != -1:
  p=float(input("Enter item price or -1 when finished: "))
  if p>0:
    t+=p
    c+=1
print("\nTotal purchase amount is %.2f"%t)
pm=float(input("\nYour payment: "))
print("\nYou bought %d items today."%c)
print("Your change is %.2f baht."%(pm-t))
