def isEven(number):
    return number %2 ==0

def isOdd(number):
    return number %2 ==1

def isPrime(number):
#number should be greater than 1
    if(number> 1):
#check for any factor exist till half of the number
        for index in range(2,number//2):
#factor exist then return false
            if(number % index == 0):
                return False
        return True
    else:
     return False


#main driver program
inputFile = open("06.06 Numbers.txt")
outputEven = open("6.6 Evennumbers.txt","w+")
outputOdd = open("6.6 Oddnumbers.txt","w+")
outputprime = open("6.6 Primenumbers.txt","w+")

#iterate over lines in n umbers.txt
for line in inputFile:
    line = int(line.strip())
#if even write in even file
    if isEven(line):
        outputEven.write(str(line) + "\n")
    elif isOdd(line): #if odd write in odd file , i just used it but not required only else will also work
        outputOdd.write(str(line) + "\n")

if isPrime(line):
    outputprime.write(str(line) + "\n")