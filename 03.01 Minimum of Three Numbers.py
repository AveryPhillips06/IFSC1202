#Minimum of Three
a = int(input("Enter Number first:"))
b = int(input("Enter Number second:"))
c = int(input("Enter Number Third:"))
def min(a, b, c):
 
    if (a < b) and (a <c):
        smallest = a
 
    elif (b < a) and (b < c):
        smallest = b
    else:
        smallest = c
         
    return smallest
 
 
print(min(a, b, c))