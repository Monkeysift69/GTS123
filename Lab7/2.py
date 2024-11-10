list1 = []

while True:
    a = input("Input: Enter a word:")
    if a == 'exit':
        break
    a = a.capitalize()
    list1.append(a)
    
print(list1)