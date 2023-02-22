from math import pi
def diameter(radius):
    return radius * 2

def circumference(radius):
    return 2 * pi * radius

def area(radius):
    return pi * radius * radius
print("{:>15s} {:>15s} {:>15s} {:>15s}".format("Radius","Diameter","Circumference","Area"))
file1 = open("06.01 Radius.txt")
line = file1.readline() 
while line != '':
    radius = float(line)
    print("{:>15.5f} {:>15.5f} {:>15.5f} {:>15.5f}".format(radius,diameter(radius),circumference(radius),area(radius)))
    line = file1.readline() 

file1.close()
