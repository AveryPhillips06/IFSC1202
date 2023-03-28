#First we create the file object to hold the file to be read
#Then we open the file in red mode.
#You can provide the full path of the file or just the file name if it,s in the same directory
#the additional r in the beginning is to convert it to a raw string.
file = open(r"C:\Users\user\Desktop\Chegg QnA\09.04 Conversion.txt","r")
#readlines() saves the lines as a list of strings
table = file.readlines()
#next we split the lines into words and convert the float values in the table from string to float
for l in range(len(table)):
    table[l] = table[l].split(" ")
    if(l!=1):
        for e in table[l][1:]:
            e = float(e)
#since the first column and row are for units only, the 1st element will be empty
table[0].insert(0,None)
#Take input from the user
from_val = float(input("Enter From Value:"))
from_unit = input("Enter From Unit:")
to_unit = input("Enter To Unit:")
flag = 0#The flag is used to detect whether the element was found in the list or not.
#Otherwise you can use the Try Except Else method too
from_unit_index = 0
to_unit_index = 0
#iterate through the elements of the table's first row and column to find the units
#also, we start from index of 1 because we know that the first row/column can be avoided and that table[0][0] will give an error since it contains a null object
for i in range(1,len(table)):
    if(table[i][0]==from_unit):
        from_unit_index = i
        flag = 1
        break
if(flag==1):
    flag = 0#resetting the flag
    for i in range(1,len(table[0])):
        if(table[0][i]==to_unit):
            to_unit_index = i
            flag = 1
            break
    if(flag==1):
        ans = table[from_unit_index][to_unit_index]*from_val
        ans = round(ans,7)
        print(ans)
    else:
        print("ToUnit is not valid")
else:
    print("FromIndex is not valid")