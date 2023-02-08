number = int(input("Enter a number:"))
#print(number%10)
#print(number%100//10)
units = number % 10
number = number // 10
tens = number % 10
hundreds = number // 10
print(units + tens + hundreds)





