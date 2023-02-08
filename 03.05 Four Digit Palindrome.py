# Taking a 4-digit number
N = int(input("Enter a Number: "))

units = N % 10
tens = (N // 10) % 10
hundreds = (N // 100) % 10
thousands = (N // 1000) % 10

if units == thousands and tens == hundreds:
    print("YES")
else:
    print("NO")