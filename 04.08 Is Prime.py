def primeno(s,e): #function start
    for i in range(s, e+1): #for loop start for given interval
        if i>1:
for k in range(2,i): #for the given no if any no which devide it or not
    if(i % k==0):
        break #break statemet
    else:
        print(i) #printing the prime no

#function block end

if __name__ == "__main__": #main
    start=int(input()) #user input1 for starting interval
    end=int(input()) #user input2 for end interval
    primeno(start,end) #calling function