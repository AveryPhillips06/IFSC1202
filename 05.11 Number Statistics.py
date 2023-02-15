
count = 0
total = 0
minvalue = 1000000
maxvalue = -1000000

valid = True

while valid:
    
    number = float(input("Enter a Value (zero to quit): "))
    

    if number == 0:
        valid = False
        break
    
    count += 1
    
    total += number
    
    if number <= minvalue:
        
        minvalue = number
    
    if number >= maxvalue:
        
        maxvalue = number

if count != 0:
    
    print("{:<10}: {}".format("Count",count))
    print("{:<10}: {}".format("Sum",total))
    print("{:<10}: {}".format("Average",total/count))
    print("{:<10}: {}".format("Minimum",minvalue))
    print("{:<10}: {}".format("Maximum",maxvalue))
