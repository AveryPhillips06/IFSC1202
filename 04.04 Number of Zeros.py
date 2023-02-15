N = int(input("Enter N: "))
i = 0
counter = 0
while i<N:
    number = int(input("Enter Number: "))
    if number == 0:
        counter = counter + 1
    i = i+1
print("Number of Zeros: {}".format(counter))
