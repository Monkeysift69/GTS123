Initial_Balance = int(input("Enter the initial balance: "))
Current_Balance = Initial_Balance
while True:
    Type_Amount = input('Transaction type and amount("done 0" to exit)').split()
    Type = Type_Amount[0]
    Amount = Type_Amount[1]
    if Type_Amount[0] == 'done' and Type_Amount[1] == '0':
        print("Current balance = %d THB" %Current_Balance)
        break
    else:
        if Amount.isnumeric():
            Amount = int(Amount)
            if Type == 'D':
                Current_Balance += Amount
                print("Deposit = %d THB, current balance = %d THB." %(Amount, Current_Balance))
            elif Type == 'W':
                if Current_Balance >= Amount:
                    Current_Balance -= Amount
                    print("Withdrawal = %d THB, current balance = %d THB." % (Amount, Current_Balance))
                else:
                    print("> Invalid transaction! Not enough balance.")

            else:
                print("> Invalid transaction!")
        else:
            print("> Invalid transaction!")
        