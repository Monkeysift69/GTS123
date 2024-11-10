import math

a = input("Start number: ")
b = input("End number: ")
c = input("Step number: ")
an = 0
cp = 0
num = ""
if a.isnumeric() and b.isnumeric() and c.isnumeric():
  a = int(a)
  b = int(b)
  c = int(c)
  if a >= 1 and b > a and c >= 1:

    for i in range(a,b+1,c):
      an += 1
      if i > 1:
        t = True
        for j in range(2, int(math.sqrt(i)+1)):
        
          if i % j == 0:
            t = False
            break
          
        if t:
            cp += 1
            num += "%d*"%(i)
        else:
            num += "%d"%(i)
      if i == 1:
          num += "%d"%(i)
      if i + c <= b:
          num +=", "
    print("Starting from %d and ending at %d with a step of %d, there are a total of %d numbers."%(a,b,c,an))
    print("Among them, %d are prime."%(cp))
    print("Numbers: %s"%(num))
  else:
    print("Input ERROR!!")
else:
  print("Input ERROR!!")