x = input('enter the values seperated bye spaces:  ')
list = x.split(" ")
max = list [0]
l=len(list)
for i in range(1):
    if list [i]>max:
        max = list [i]
x = list.index(max)
min = list [0]
for i in range(l):
    if list [i]<min:
        min = list [i]
y = list.index (min)
list [x] = min
list [y] = max
final = ' '.join(list)
print("swap minimum and maximum:  ".final)

