A = int(input("Enter A: "))
B = int(input("Enter B: "))
for i in range(A, B + 1):
    if i > 1:
        for j in range(2, int(i / 2) + 1):
            if (i % j) == 0:
                break
        else:
            print(i)