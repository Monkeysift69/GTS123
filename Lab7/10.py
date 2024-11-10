n=input("Enter an integer number ('X' to exit): ")
if n.isnumeric():
  n=int(n)
  i,j=0,0
  while i<n:
    while j<n:
      if i==j or i+j==n-1:
        print("X",end=" ")
      else:
        print(".",end=" ")
      j+=1
    i+=1
    j=0
    print()