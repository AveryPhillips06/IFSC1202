#accepting length of Race
length=int(input("Enter Length of Race in Kilometers: "))
#accepting Minutes
minute=int(input("Enter Minutes: "))
#accepting Seconds
second=int(input("Enter Seconds: "))
#printing average speed
print((length/((minute*60+second)/3600))/1.61)