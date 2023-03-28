
with open("09.06 CityTemps.txt", 'r') as file:
    temps = []  # initializing temps list to store data

    line = file.readline()
    while line:
        row = line.split()
        temps.append(row)  # appending list to temps list
        line = file.readline()   # read next line

for i in range(len(temps)):
    total = 0    

    for temp in temps[i][1:]:
        total = total + float(temp)   # adding temperature to total

    average = total / (len(temps[i]) - 1)
    temps[i].append(int(average))  # appending average to temps list
print(f"{'City' : <10}{'Mo' : <10}{'Tu' : <10}{'We' : <10}{'Th' : <10}{'Fr' : <10}{'Sa' : <10}{'Su' : <10}{'Avg' : <10}")
  
for i in range(len(temps)):
    for j in range(len(temps[0])):
        print(f"{temps[i][j] : <10}", end='')
    print("")