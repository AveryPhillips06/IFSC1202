N = int(input("Enter N: "))
flag = True
if N > 1:
    for i in range(2,int((N/2))+1):
        if N%i == 0:
            print("COMPOSITE")
            break
    else:
        print("PRIME")
else:
    print("COMPOSITE")