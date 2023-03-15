num = input("Enter values separated by spaces: ").split()
for i in range(0, len(num), 2):
    if i+1 < len(num):
        num[i], num[i+1] = num[i+1], num[i]
print("Swapped Values: ", end='')
for item in num:
    print(item, end=' ')
print()