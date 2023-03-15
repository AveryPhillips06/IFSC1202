min = 0
max = 0 
x = input('enter the values seperated bye spaces:  ')
list = x.split()
for i in range(1,len(list)):
    if int(list[i]) > int(list[max]):
        max = i
    if int(list[i]) < int(list[min]):
        min = i
temp = list[min]
list[min] = list[max]
list[max] = temp
print("swap minimum and maximum:  ",end = " ")
for i in range(len(list)):
    print(list[i], sep= " ", end = " ")
print()



