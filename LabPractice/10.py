# Exchange rate conversion table
rates = {
    'JPY': 0.29,
    'USD': 31.99,
    'EUR': 35.62
}

money = []
cur = []
rmoney = []

while True:
    x = input("Input: ")
    if x.lower() == 'end':
        break
    tokens = x.strip().split()
    if len(tokens) != 2:
        print("ERROR")
        continue
    currency = tokens[0].strip().upper()
    amount_str = tokens[1].strip()
    try:
        amount = float(amount_str)
        if amount < 1:
            print("ERROR")
            continue
    except ValueError:
        print("ERROR")
        continue
    if currency not in rates:
        print("ERROR")
        continue
    # Valid input; store the data
    cur.append(currency)
    money.append(amount)
    # Calculate the converted amount and store it
    converted_amount = amount * rates[currency]
    rmoney.append(converted_amount)

# Now, display the results
for k, i, j in zip(money, cur, rmoney):
    print("%.2f %s is %.2f THB" % (k, i, j))
""""
# Exchange rate conversion table
rates = {
    'JPY': 0.29,
    'USD': 31.99,
    'EUR': 35.62
}

money = []
cur = []
rmoney = []

while True:
    x = input("Input: ")
    if x.lower() == 'end':
        break
    tokens = x.strip().split()
    if len(tokens) != 2:
        print("ERROR")
        continue
    currency = tokens[0].strip().upper()
    amount_str = tokens[1].strip()
    try:
        amount = float(amount_str)
        if amount < 1:
            print("ERROR")
            continue
    except ValueError:
        print("ERROR")
        continue
    if currency not in rates:
        print("ERROR")
        continue
    # Valid input; store the data
    cur.append(currency)
    money.append(amount)
    # Calculate the converted amount and store it
    converted_amount = amount * rates[currency]
    rmoney.append(converted_amount)

# Now, display the results
for k, i, j in zip(money, cur, rmoney):
    print("%.2f %s is %.2f THB" % (k, i, j))

"""