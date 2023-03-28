def print_list(a):
    for row in a:
        for elem in row:
            print(elem, end=' ')#prints space after each element
        print()#newline
def scale_list(a,s):
    for i in range(len(a)):
        for j in range(len(a[i])):
            a[i][j]=s*a[i][j]#multiply scalar with the element
    return a
ins = open( "09.03 NumbersList.txt", "r" )
a = []
for line in ins:
    number_strings = line.split() # Split the line on runs of whitespace
    numbers = [int(n) for n in number_strings] # Convert to integers
    a.append(numbers) # Add the "row" to your list.
print_list(a)
s=int(input("Enter the scalar value : "))
a=scale_list(a,s)
print_list(a)