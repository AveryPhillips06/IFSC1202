#get inputs from user
firstNumber=int(input("Enter First 2 Digit Number:"))
secondNumber=int(input("Enter Second 2 Digit Number:"))
a = int(firstNumber%100//10)
b = int(firstNumber%10)
c = int(secondNumber%100//10)
d = int(secondNumber%10)
#print(number%10)
#print(number%100//10)#
#b = int(number%10)
#a = int(number%100//10)
#c = int(number%1000//100)
print(a,c,b,d)
