#Minimum of Three
a = int(input("Enter Number first:"))
b = int(input("Enter Number second:"))
C = int(input("Enter Number Third:"))
def maximum(a, b, c):
 
    if (a >= b) and (a >= c):
        largest = a
 
    elif (b >= a) and (b >= c):
        largest = b
    else:
        largest = c
         
    return largest
 
 
print(maximum(a, b, c))