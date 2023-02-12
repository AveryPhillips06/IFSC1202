largest = 0
occurrences = 0
firstNumber = True
while True:
    num = int(input('Enter a Number (zero to quit): '))
    if num == 0: break
    if firstNumber or largest < num:
        largest = num
        occurrences = 1
    elif largest == num:
        occurrences += 1
    firstNumber = False
print('Maximum:', largest)
print('Number of Occurrences:', occurrences)