num = 1
previous = 0
i = 0
count = 0
best = None
max_count = 0

while num != 0:
    num = int(input("Enter a Number (zero to quit): "))
    if num != 0:
        if i == 0:
            previous = num
            count = 1
        else:
            if num == previous:
                count += 1
            else:
                if count > max_count:
                    max_count = count
                    best = previous
        i += 1
        previous = num

print(best, "repeated", max_count, "times")