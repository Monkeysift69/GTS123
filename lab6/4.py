namelist=['Satawat', 'Pisit', 'Thanaphong', 'Pished', 'Nut', 'Amon']


for i in namelist:
  print("Student list:", namelist)
  remove=input("Please enter the student's name you want to delete: ")
  if remove=='q':
    break
  else:
    print("You will delete ' %s ' from this class"%remove)
    x = input("Please type (Confirm 'y', cCancel 'n': )")
    if x == "y":
        for i, x in enumerate(namelist):
            if x==remove:
                namelist.pop(i)


# Use While Loop (not learned yet)

"""name = ["Satawat", "Pisit", "Thanaphong", "Pished", "Nut", "Amon"]

a = True

while a:
    print("Student list: %s" %name)
    a = input("Please enter a student's name that you want to delete (q = exit): ")
    if a == "q": a = False
    else: 
         print("You will delete ' %s ' from this class"%a)
         x = input("Please type (Confirm 'y', cCancel 'n': )")
         if x == "y": name.remove(a)
         else: pass"""