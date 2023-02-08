# Taking a 4-digit number as input from user and cast it to integer type
N = int(input("Enter a Number: "))

# Calculations for the units, tens, hundreds and thousands digit
units = N % 10
tens = (N // 10) % 10
hundreds = (N // 100) % 10
thousands = (N // 1000) % 10

# Condition to check for Palindrome
if units == thousands and tens == hundreds:
    # Print YES, if the number is a palindrome
    print("YES")
else:
    # Print NO, if the number is not a palindrome
    print("NO")