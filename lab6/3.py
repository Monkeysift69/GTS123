list1 = []

for i in range(5):
    i+=1
    x = int(input("input #%d : " %i))
    list1.append(x)

summ = sum(list1)
average = summ/(len(list1))
min = min(list1)
max = max(list1)

a = input("Select the option: 10 Summary, 2) average, 3) min, 4) max....")

if a == '1': print("Your result is %d" %summ)
elif a == '2': print("Your result is %d" %average)
elif a == '3': print("Your result is %d" %min)
elif a == '4': print("Your result is %d" %max)