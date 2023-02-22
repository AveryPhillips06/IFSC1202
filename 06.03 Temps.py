file = open("06.03 FTemps.txt") #opens file 06.03 FTemps.txt to read
records = 0 #initializing the variable records to zero
for F in file: #loop for data in file
    C = (float(F) - 32)*5/9 #convert fahrenheit to celsius
    C = round(C,1) #round off C to 1 decimal place
    f = open("06.03 CTemps.txt", "a") #opens file 06.03 CTemps.txt to write
    f.write(str(C)) #convert C to string to write in file
    f.write('\n') #goes to new line
    f.close() #closes the file
    records = records + 1 #increase records by 1

print(str(records)+" records written") 
