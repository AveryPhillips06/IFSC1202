num = 1
previous = 0
i = 0
count = 0

while num != 0:
    num = int(input("Enter a Number (zero to quit): "))
    if num != 0:
        if i == 0:
            previous = num
        if num > previous:
            count += 1
        i += 1
        previous = num

print("Number of Values Greater Than the Previous:", count)