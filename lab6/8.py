x = input("Enter a string: ").split()
list1 = []
for word in x:
    rv = word[::1].swapcase()
    list1.append(rv)

print("Rever string output:", " ".join(list1))