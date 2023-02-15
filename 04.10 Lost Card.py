N=int(input('Enter Number of Cards:'))

A=[]
x=0
for i in range(1,N):
    x=int(input('Enter Card:'))
A.append(x)
s1=0
for i in range(1,N+1):
    s1=s1+i


s2=0
for i in range(len(A)):
    s2=s2+A[i]

s=s1-s2
print('Missing Card:', s)