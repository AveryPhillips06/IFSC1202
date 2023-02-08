#Distance to Closest
A = int(input("Enter point A:"))
B = int(input("Enter point B:"))
C = int(input("Enter point C:"))
D = abs(A-B)
E = abs(A-C)
    
if(D>E):
    print(E)
else:
    print(D)