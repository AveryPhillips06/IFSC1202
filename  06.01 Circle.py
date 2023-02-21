import math

# diameter method
# accept the radius as a parameter
# and returns the diameter of the circle
def diameter(radius):
    return radius * 2

# circumference mehtod
# accept the radius as a parameter
# and returns the circumference of the circle
def circumference(radius):
    return 2 * math.pi * radius


# area method
# accept the radius as a parameter
# and returns the area of the circle
def area(radius):
    return math.pi * radius * radius


# main method
def main():

    # open a file to read
    file1 = open("06.01 Radius.txt","r")

    # create a empty list to store all the radius from the file
    lst = []

    # infinite while loop
    # to read line by line from the file
    while True:
        line = file1.readline()
        if not line:
            break
        else:
            lst.append(float(line))

    # print the radius diameter , circumference and area of the circle
    print("{:>15} {:>15} {:>15} {:>15}".format("Radius","Diameter","Circumference","Area"))
    for radius in lst:
        print("{:>15.5f} {:>15.5f} {:>15.5f} {:>15.5f}".format(radius,diameter(radius),circumference(radius),area(radius)))



if __name__ == "__main__":
    main()