fruits = ['Apple', 'Banana', 'Orange', 'Grape', 'Mango', 'Kiwi']

for i in fruits:
    l = len(i)

    if l >= 6:
        print("%s is 6 characters or more!" %i)
    else:print("%s is only %d long!"% (i, l))