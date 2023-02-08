#get inputs from user
firstNumber=int(input("Enter First 2 Digit Number:"))
secondNumber=int(input("Enter Second 2 Digit Number:"))
a = int(firstNumber%100//10)
b = int(firstNumber%10)
c = int(secondNumber%100//10)
d = int(secondNumber%10)

print(a,c,b,d)
