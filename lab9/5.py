def CelsiusToFahrenhiet(c):
    f = (c*(9/5))+32
    return f

x = int(input("Input temperature in degree Celcius: "))
print("The degree in Farenheit is %.2f" %CelsiusToFahrenhiet(x))