characters = []

while len(characters) < 9:
    char = input("Input: ")
    
    if char == 'x' or char == 'o':
        characters.append(char)
    else:
        print("Wrong input")
        break


if len(characters) == 9:

    print("-------") # 0 3 6
    for i in range(0, 9, 3):
        print("|%s|%s|%s|" % (characters[i], characters[i+1], characters[i+2]))
        print("-------")