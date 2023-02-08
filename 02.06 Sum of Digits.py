number = int(input("Enter a 3 Digit Number:"))#take int type input
add = 0 #initialize the add variable which stores the sum to 0
for i in range(0,3):#loop through 0 to 3 i.e. 3 digits
add += number%10#find the modulo so that you get the last digit of the 3 digit number
number = number//10#divide the by 10 so that you get the remaining digits

print("Sum of Digits: {}".format(add))#print the sum of digits using the format