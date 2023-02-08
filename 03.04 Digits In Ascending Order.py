number = int(input('Enter a number: '))
digits = []
while(number != 0):
    n = int(number%10)

digits.append(n)

number = int(number/10)
flag = 0

for i in range(2):
if(digits[i] < digits[i+1]):
    flag = 1
break

if flag == 1:
    print('NO')
else:
    print('YES')