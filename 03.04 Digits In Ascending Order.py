#asking the user to enter a number
number = int(input('Enter a number: '))
#list to hold the digits of the entered number
digits = []

#running a while loop to fill the list with the digits of the number
while(number != 0):
#extracting the last digit from the number
n = int(number%10)
#adding that digit to the list
digits.append(n)
#reducing the number of digits of the number
number = int(number/10)
#here we get a list of digits in right to left order


flag = 0
#loop to check if they are ascending from left to right, for which they are descending from right to left
for i in range(2):
#checking if the digits are in descending order from right to left
if(digits[i] < digits[i+1]):
flag = 1
break

#printing the appropriate message
if flag == 1:
print('NO')
else:
print('YES')