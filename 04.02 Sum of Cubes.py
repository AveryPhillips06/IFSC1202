N = 5

# initializing k to one
k = 1

# initializing total to zero
total = 0

# looping from 1 to N
while k <= N:
    # updating the value of total
    total = total + (k * k * k)

    # incrementing the value of k by 1
    k = k + 1

print(total)