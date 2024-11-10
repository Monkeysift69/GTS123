t = True
l = []
while t:
  n = input("enter item price or -1 when finished: ")
  if n == "-1":
    t = False
  else:
    l.append(float(n))
  summ = sum(l)
print("Total purchase amount is %.2f" %summ)
p = input("Your payment: ")
p = float(p)
print("You bought %d items today" %len(l))
print("Your change is %.2f baht." %(p-summ))