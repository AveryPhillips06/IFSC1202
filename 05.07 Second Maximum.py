m = int(input("\nEnter First Number: "))
sm = int(input("Enter Second Number: "))

if sm > m:
    m, sm = sm, m

n = int(input("Enter a Number (zero to quit): "))

while( n != 0 ):
    if n > m:
        m, sm = n, m
    elif n > sm:
        sm = n
n = int(input("Enter a Number (zero to quit): "))

print("\nFirst Maximum:",m)
print("Second Maximum:",sm)
print("")