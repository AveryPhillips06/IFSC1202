s = input("Enter Values Separated by Space: ")
lst = s.split(" ")
for x in range(len(lst)):
    if int(lst[x])%2==1:
        print(lst[x])