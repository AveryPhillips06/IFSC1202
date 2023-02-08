a=int(input("Enter 1st number:"))
b=int(input("Enter 2nd number:"))
c=int(input("Enter 3rd number:"))
if(a==b==c):
    print(3)

elif ((a==b and a!=c) or (b==c and c!=a) or (a==c and c!=b)):

    print(2)
elif (a!=b!=c):
    print (0)

