st=input('Enter a string: ')
n=len(st)
s1=""
s2=""
for i in range(0,(n+1)//2):
    s1+=st[i]
for i in range((n+1)//2,n):
    s2+=st[i]
print(s2,end='')
print(s1)
