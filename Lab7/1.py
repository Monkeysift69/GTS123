list1 = []


while True:
    a = input("Input: Enter a word:")
    if a == 'exit':
        break
    if a[-1] == 'y':
        a=a.replace('y', 'ily')
        list1.append(a)
    
    else:
        list1.append(a)
    
print(list1)