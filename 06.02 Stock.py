#opening Stock.txt file for reading
inputFile = open("Stock.txt","r")

#reading data from Stock.txt into float list
data = inputFile.read()
data = [float(i) for i in data.split()]

#printing header
print("Price Change")

#printing first value
print(data[0])

#traversing through the list
for i in range(1,len(data)):

    #calculating percentage change
    percentage = ((data[i] - data[i-1])/data[i-1]) * 100

#printing formated output
print("{:.2f} {:+.2f}%".format(data[i],percentage))