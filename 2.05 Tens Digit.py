#program to print tens digit of a number
n=input('Enter a Number : ');
tensDigit=(int(n)/10)%10; #converting n to int
print('Tens Digint: ', format(int(tensDigit))) #converting float to int and int to .format
