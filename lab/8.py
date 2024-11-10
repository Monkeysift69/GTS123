x = input()

if x.isnumeric():
    x = int(x)
    if x >= 3:
        # Top half of the butterfly
        for i in range(x):
            # Left part of the butterfly
            for j in range(x):
                if j <= i:
                    if j % 2 == 0:
                        print("*", end="")
                    else:
                        print("0", end="")
                else:
                    print(" ", end="")
            
            # Right part of the butterfly
            for j in range(x-1, -1, -1):
                if j <= i:
                    if j % 2 == 0:
                        print("*", end="")
                    else:
                        print("0", end="")
                else:
                    print(" ", end="")
            
            print()

        # Bottom half of the butterfly
        for i in range(x-2, -1, -1):
            # Left part of the butterfly
            for j in range(x):
                if j <= i:
                    if j % 2 == 0:
                        print("*", end="")
                    else:
                        print("0", end="")
                else:
                    print(" ", end="")
            
            # Right part of the butterfly
            for j in range(x-1, -1, -1):
                if j <= i:
                    if j % 2 == 0:
                        print("*", end="")
                    else:
                        print("0", end="")
                else:
                    print(" ", end="")
            
            print()
