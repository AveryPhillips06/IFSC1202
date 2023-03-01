
inputFile = open("06.02 Stock.txt")
data = float(inputFile.readline())
print("Price   Change")
print(data)
yesterday = data

data = float(inputFile.readline())
while data != "":
    data = float(data)
    percentage = ((data - yesterday)/yesterday) * 100
    print("{:.2f} {:+.2f}%".format(data,percentage))
    yesterday = data
    data = inputFile.readline()

    