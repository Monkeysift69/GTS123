
from operator import itemgetter

coffeeDB = [['A','Americano',120],['M','Matcha Latte',125],['C','Signature Chocolate',130],['E','Espresso',50],['O','Sai Nam Pueng Orange Juice',95],['R','Iced Raspberry Juice Tea',115]]

#### Task 1: Utilize the sorted() function to create a new variable sorted in descending order by price, which can be utilized for printing.
menusorted = sorted(coffeeDB, key=itemgetter(2), reverse=True)


print("Beverage Menu")
print("-"*56)
print("| %-3s | %-4s | %-30s | %-6s |" % ("No.","Code","Item Name","Price"))
print("-"*56)
for i, val in enumerate(menusorted):
    print("| %2d. | %-4s | %-30s | %6.2f |" % (int(i+1),val[0],val[1],val[2]))
print("-"*56)


menucode = [i[0] for i in coffeeDB]


userorder = input("User's orders: ")

summ_item = []
for a in userorder:
    if a.upper() in menucode:

        #check exist

        found = -1
        for i, b in enumerate(summ_item):
            if b[0] == a.upper():
                found = i 
            
### Task 2: The variable summ_item is designed to store menu codes and quantities.
### If the variable "found" is greater than or equal to 0, it indicates that the menu code exists in summ_item with an index equal to found. In this case, you should update the quantity.
### If the variable "found" is negative, it indicates that no menu code is found in summ_item. In this case, you should add the user's order.


        #### CODE HERE ####
    
        if found >= 0:
            summ_item[found][1]+=1
        elif found < 0:
            summ_item.append([a.upper(),1])
    else:
        print("skipping NOCODE (%s)" % a)

if len(summ_item) > 0:
    print("Bill summary")
    print("-"*56)
    print("| %-3s | %-30s | %-4s | %-6s |" % ("NO.","ITEM NAME","QTY","AMOUNT"))
    print("-"*56)
    total = 0
    for i, val in enumerate(summ_item):

        menudetail = [[d[1],d[2]] for d in coffeeDB if val[0] == d[0]] # Item and price from coffeDB

        #### Task 3: Complete the calculation for "menuprice", "qty", and "total".
        #### CODE HERE ####
        #### also FIX BELOW ####

        menuprice = menudetail[0][1] #nested list
        qty = val[1]
        amount = menuprice * qty
        total += amount

        print("| %2d. | %-30s | %-4s | %6.2f |" % (i+1,menudetail[0][0],qty,amount))
    print("-"*56)


    #### Task 4: Conclude the summary at the end of the bill with a VAT rate of 7%.
    #### CODE HERE ####
    #### also FIX BELOW ####

    print("| %-43s | %6.2f |" % ("Subtotal", total) )
    print("| %-43s | %6.2f |" % ("Total tax", total*(7/100)) )
    print("| %-43s | %6.2f |" % ("Total",total+total*(7/100)) )
    print("-"*56)
else:
    print("NO ORDER!!!")

