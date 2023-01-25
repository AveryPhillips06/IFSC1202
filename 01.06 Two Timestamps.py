# Read an integer:
a = int(input(Hour))

# Read a int:
b = int(input(Minutes))

# Read a int:
c = int(input(Seconds))
d = int(input(Hour 2))
e = int(input(Minutes 2))
f = int(input(Seconds))
# calculating total number of seconds
seconds = a*3600 + b*60 + c - d*3600 + e*60 + f

# printing result
print(seconds)