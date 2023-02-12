evens = 0
while True:
    num = int(input('Enter a Number (zero to quit): '))
    if num == 0: break
    if num % 2 == 0: evens += 1
print('Number of Even Values:', evens)
