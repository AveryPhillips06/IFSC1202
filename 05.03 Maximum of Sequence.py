largest = 0
firstNumber = True
while True:
    num = int(input('Enter a Number (zero to quit): '))
    if num == 0: break
    if firstNumber or largest < num:
        largest = num
    firstNumber = False
print('Maximum:', largest)