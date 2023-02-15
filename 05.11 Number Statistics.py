# declare initial variables to store the data
count = 0
total = 0
minvalue = 1000000
maxvalue = -1000000

# the valid flag to control the loop
valid = True

# asks the user to enter the number until valid flag is true
while valid:
    
    # get the number from the user    
    number = float(input("Enter a Value (zero to quit): "))
    
    # if the entered number is 0 then set valid to false and break the loop
    if number == 0:
        valid = False
        break
    
    # increment the count variable by 1
    count += 1
    
    # add the entered number in total variable
    total += number
    
    # if the entered number is lower than the minvalue
    if number <= minvalue:
        
        # update the minvalue
        minvalue = number
    
    # if the entered number is higher than the maxvalue
    if number >= maxvalue:
        
        # update the maxvalue
        maxvalue = number

# if count is not 0
if count != 0:
    
    # display the output
    print("{:<10}: {}".format("Count",count))
    print("{:<10}: {}".format("Sum",total))
    print("{:<10}: {}".format("Average",total/count))
    print("{:<10}: {}".format("Minimum",minvalue))
    print("{:<10}: {}".format("Maximum",maxvalue))
