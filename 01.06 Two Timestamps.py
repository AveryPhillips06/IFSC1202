# Read an integer:
a = int(input(Hour))

# Read a int:
b = int(input(Minutes))

# Read a int:
c = int(input(Seconds))
d = int(input(hour))
e = int(input(minutes))
f = int(input(seconds))
# calculating total number of seconds
seconds = a*3600 + b*60 + c - d*3600 + e*60 + f

# printing result
print(seconds)