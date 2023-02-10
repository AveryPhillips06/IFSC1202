N=int(input('Enter Number of Cards:'))

#reading each card and creating an array containing them
A=[]
x=0
for i in range(1,N):
    x=int(input('Enter Card:'))
A.append(x)

#sum of the values from 1 to N (Total Value of Cards)
s1=0
for i in range(1,N+1):
    s1=s1+i

#sum of the values on remaining cards (sum of elements of array A)
s2=0
for i in range(len(A)):
    s2=s2+A[i]

#value on the lost card
s=s1-s2
print('Missing Card:', s)