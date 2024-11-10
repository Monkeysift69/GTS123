a=input("Input: ").split(",")
for i in a:
  for j in a:
    if i<j:
      for k in a:
        if i<j and j<k and i<k:
          print(i,j,k)