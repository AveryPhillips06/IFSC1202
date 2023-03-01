def isEven(n):
    return (n%2==0)
def isOdd(n):
    return (n%2)
def isPrime(n):
    if(n > 1):
        for i in range(2,n//2):
            if(n%i==0):
                return False
        else:
            return True
    else:
        return False
file1 = open('06.06 Numbers.txt','r')
file2 = open('6.6 Evennumbers.txt','w')
file3 = open('6.6 Oddnumbers.txt','w')
file4 = open('6.6 Primenumbers.txt','w')
nums = file1.readlines()
evencount = 0
oddcount = 0
primecount = 0
readcount = 0
for line in nums:
    n = int(line.strip())
    if(isEven(n)):
        file2.write(str(n)+"\n")
        evencount += 1
    elif(isOdd(n)):
        file3.write(str(n)+"\n")
        oddcount += 1
    if(isPrime(n)):
        file4.write(str(n)+"\n")
        primecount += 1
readcount += 1
print("{} even numbers".format(evencount))
print("{} odd numbers".format(oddcount))
print("{} prime numbers".format(primecount))
print("{} read numbers".format(readcount))
file1.close()
file2.close()
file3.close()
file4.close()