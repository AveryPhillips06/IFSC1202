def fractional(num):
    number = float("0."+str(num).split(".")[1])
    print(f"Fractional Part: {number}")


num = float(input("Enter a Number: "))
fractional(num)