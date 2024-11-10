while True:
    number = input("Enter an integer number (0 to exit): ")
    size = int(number)
    if size == 0:
        print("Exit program. Bye!")
        break
    else:
        if size >= 9:
            print("Valid value is between 0 and 9")
            break
        else:
            if number.isnumeric():
                for i in range(1, size + 1):
                    print(' ' * (size - i) + (number + ' ') * i)
                
            else:
                print("Valid value is between 0 and 9")
                break