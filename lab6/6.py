a = input("Enter dd/mm/yyyy: ")

d = a[:2]
m = a[2:4]
y = a[4:]

l = len(a)


if l != 8:
    print("Please enter 8 digits")
else:

    if m > "12":
        print("Error There're 12 months")
    else:
        print("Date = %s\nMonth = %s\nYear = %s"%(d,m,y))