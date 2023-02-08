a=int(input("NO1: "))
b=int(input("NO2: "))
c=int(input("NO3: "))
if a<b and a<c:
    if b<c:
        x,y,z=a,b,c
    else:
        x,y,z=a,c,b
elif b<a and b<c:
    if a<c:
        x,y,z=b,a,c
    else:
        x,y,z=b,c,a
else:
    if a<b:
        x,y,z=c,a,b
    else:
        x,y,z=c,b,a
print("numbers in ascending order: ",x,y,z)