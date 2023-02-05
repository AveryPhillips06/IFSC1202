#Statement to import array
import array as array
#get inputs from user
firstNumber=int(input("Enter First 2 Digit Number:"))
secondNumber=int(input("Enter Second 2 Digit Number:"))
#Convert the individual elements into array
a=arr.array('i',[int(firstNumber/10),int(secondNumber/10),int(firstNumber%10),int(secondNumber%10)]);
#merge array to string
merged=''.join(map(str,a));
#print the result
print("Merged Number:",merged)