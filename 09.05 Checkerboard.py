def find_row(size):
    first_row=[]
    for i in range(size):
    #checking for first row or last row 
    #then we need to add +  and - 
        if i==0 or i==size-1:
            first_row.append('+')
        else:
            first_row.append('-')
    return first_row        
        
n=int(input("Enter Size :"))
size=n+2
l=[]
#attaching our firs row to the list 
l.append(find_row(size))
#we have done with first and last row 
#do the middle part 1 to size-1
for i in range(1,size-1):
    column=[]                
    for j in range(size):
        if j==0 or j==size-1:
            column.append('|')
        else:
            if(i%2==0):              #row is even 
                if(j%2==0):
                    column.append(' ')
                else:
                    column.append('*')
            else:                     #row  is odd
                if(j%2==0):
                    column.append('*')
                else:
                    column.append(' ')   
                    
    l.append(column)   ##append each row in a after each iteration
#call find row that is same as first_row and append to list to last row 
l.append(find_row(size))  

 #now list has everthing so convert the list to pattern 
o=""
for i in range(size):
    o+=''.join(l[i])        
    o+='\n'                 
print(o)