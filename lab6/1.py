a=input("Input: ").split(",")
for i in a:
  for j in a:
    if i!=j:
      for k in a:
        if k!=i and k!=j:
          print(i,j,k)