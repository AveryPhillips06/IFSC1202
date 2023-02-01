print ("first time stamp")
a = int(input("Hour:"))

# Read a int:
b = int(input("Minutes:"))

# Read a int:
c = int(input("Seconds:"))
print ("second time stamp")
d = int(input("Hour:"))
e = int(input("Minutes:"))
f = int(input("Seconds:"))
# calculating total number of seconds
seconds = (d*3600 + e*60 + f) - (a*3600 + b*60 + c)

# printing result
print(seconds)