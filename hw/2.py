word = {}
while True:
    a = input("Enter a line (or 'END' to finish): ")
    if a.lower() == 'end':
        break

    a = a.replace(',', '')
    a = a.replace('.', '')
    a = a.split()

    for i in a:
        i = i.lower()
        if i in word:
            word[i] += 1
        else:
            word[i] = 1

    b1 = 0
    b2 = 0
    b3 = 0

    for count in word.values():
        if count <= 2:
            b1 += 1
        elif count == 3 or count == 4:
            b2 += 1
        elif count > 4:
            b3 += 1

print("1. Number of words that appear once or twice: %d" %(b1))
print("2. Number of words that appear three and four times: %d" %(b2))
print("3. Number of words that appear more than four times: %d" %(b3))