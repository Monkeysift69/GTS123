x = True
while x:
  print("="*5,"MAIN MENU","="*5)
  print("1. Addition\n2. Subtraction\n3. Exit")
  n = input("Select an operation (1-3): ")

  if n == "1":
    a = input("Enter two number").split()
    print("%s + %s = %d"%(a[0],a[1],int(a[0])+int(a[1])))
  elif n == "2":
    a = input("Enter two number").split()
    print("%s - %s = %d"%(a[0],a[1],int(a[0])-int(a[1])))

  elif n == "3":
    x = False
