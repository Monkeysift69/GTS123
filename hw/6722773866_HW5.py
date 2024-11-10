word_counts = {}
while True:
    x = input("Enter a line (or 'END' to finish): ")
    if x.lower() == 'end':
        break

    x = x.replace(',', '')
    x = x.replace('.', '')
    x = x.split()

    for i in x:
        i = i.lower()
        if i in word_counts:
            word_counts[i] += 1
        else:
            word_counts[i] = 1

t = 0  
tf = 0  
f = 0   

for count in word_counts.values():
    if count <= 2:
        t += 1
    elif count == 3 or count == 4:
        tf += 1
    elif count > 4:
        f += 1

print("1. Number of words that appear once or twice: %d" % t)
print("2. Number of words that appear three and four times: %d" % tf)
print("3. Number of words that appear more than four times: %d" % f)