fromValue = int(input("Enter From Value : "))
fromUnit = input("Enter From Unit(in,ft,yd,mi) : ")
toUnit = input("Enter To Unit(in,ft,yd,mi) : ")

floatfromValue = float(fromValue)

if fromUnit == toUnit:
    print(str(floatfromValue) + " " + fromUnit + " => " + str(floatfromValue) + " " + fromUnit)

elif fromUnit == "in" and toUnit == "ft":
    toValue = round(fromValue / 12, 7)
    print(str(floatfromValue) + " " + fromUnit + " => " + str(toValue) + " " + toUnit)

elif fromUnit == "in" and toUnit == "yd":
    toValue = round(fromValue / 36, 7)
    print(str(floatfromValue) + " " + fromUnit + " => " + str(toValue) + " " + toUnit)

elif fromUnit == "in" and toUnit == "mi":
    toValue = round(fromValue / 63360, 7)
    print(str(floatfromValue) + " " + fromUnit + " => " + str(toValue) + " " + toUnit)

elif fromUnit == "ft" and toUnit == "in":
    toValue = round(fromValue * 12, 7)
    print(str(floatfromValue) + " " + fromUnit + " => " + str(toValue) + " " + toUnit)

elif fromUnit == "ft" and toUnit == "yd":
    toValue = round(fromValue / 3, 7)
    print(str(floatfromValue) + " " + fromUnit + " => " + str(toValue) + " " + toUnit)

elif fromUnit == "ft" and toUnit == "mi":
    toValue = round(fromValue / 5280, 7)
    print(str(floatfromValue) + " " + fromUnit + " => " + str(toValue) + " " + toUnit)

elif fromUnit == "yd" and toUnit == "in":
    toValue = round(fromValue * 36, 7)
    print(str(floatfromValue) + " " + fromUnit + " => " + str(toValue) + " " + toUnit)

elif fromUnit == "yd" and toUnit == "ft":
    toValue = round(fromValue * 3, 7)
    print(str(floatfromValue) + " " + fromUnit + " => " + str(toValue) + " " + toUnit)

elif fromUnit == "yd" and toUnit == "mi":
    toValue = round(fromValue / 1760, 7)
    print(str(floatfromValue) + " " + fromUnit + " => " + str(toValue) + " " + toUnit)

elif fromUnit == "mi" and toUnit == "in":
    toValue = round(fromValue * 63360, 7)
    print(str(floatfromValue) + " " + fromUnit + " => " + str(toValue) + " " + toUnit)

elif fromUnit == "mi" and toUnit == "ft":
    toValue = round(fromValue * 5280, 7)
    print(str(floatfromValue) + " " + fromUnit + " => " + str(toValue) + " " + toUnit)

elif fromUnit == "mi" and toUnit == "yd":
    toValue = round(fromValue * 1760, 7)
    print(str(floatfromValue) + " " + fromUnit + " => " + str(toValue) + " " + toUnit)

else:
    if (("in" not in fromUnit) and ("ft" not in fromUnit) and ("yd" not in fromUnit) and ("mi" not in fromUnit)):
        print("FromUnit is not valid")
    else:
        print("ToUnit is not valid")