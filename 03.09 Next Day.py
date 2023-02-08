def func(date):
#breaking the date into parts
month1, day1, year1 = date.split('/')
#converting the parts into integers
m1=int(month1)
d1=int(day1)
y1=int(year1)
#checking the date range values
if ((m1>=1 and m1<=12)and(d1>=1 and d1<=31) and(y1>=1600 and y1<=2400)):
f=1
#checking for leap year
if y1%4==0 or (y1%100==0 and y1%400==0):
ly=1
print(y1,"leap year")
else:
ly=0
print(y1,"not a leap year")
#checking the date is valid or not
if m1==1 or m1==3 or m1==5 or m1==7 or m1==8 or m1==10 or m1==12:
if d1>=1 and d1<=31:
vd=1
else:
vd=0
elif m1==4 or m1==6 or m1==9 or m1==11:
if d1>=1 and d1<=30:
vd=1
else:
vd=0
else:
if ly==1:
if d1>=1 and d1<=29:
vd=1
else:
vd=0
elif ly==0:
if d1>=1 and d1<=28:
vd=1
else:
vd=0
else:
f=0
if f==0 or vd==0:
return -1
else:
#converting date into datanumber
num=(1461*(y1+4800+(m1-14)/12))/4+(367*(m1-2-12*((m1-14)/12)))/12-(3*((y1+4900+(m1-14)/12)/100))/4+d1-32075
return num
while(1):
date1=input("enter first date:")
datenum1=func(date1)
if datenum1==-1:
print(date1,"is Invalid date\tre-enter valid date")
ch='yy'
else:
print(date1,"is valid date")
#if first date is valid then only reads second date
if(ch!='yy'):
date2=input("enter second date:")
datenum2=func(date2)
if datenum2==-1:
print(date2,"is Invalid date\tre-enter valid date")
ch='yy'
else:
print(date2,"is valid date")
#if second date is valid then only proceeds further
if(ch!='yy'):
x=abs(datenum2-datenum1)
print("The number of days between",date1,"and",date2,"is",int(x),"days")
ch=input("play again (y/n):")
if(ch=='n'):
print("thank you for playing")
break
else: