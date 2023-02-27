# proper case function
def ProperCase(s):
    # check if string is empty
    if s == '':
        return ''

    # upper case first character
    ch = s[0].upper()

    # return the substrings joined
    return (ch + s[1:len(s)].lower())


# remove new line function
def RemoveNewLine(s):
    return s.replace("\n", "")

# trim function
def trim(s):

    s = s.strip()

    return " ".join(s.split())

   
# first name function return first name from string s
def FirstName(s):
    s = trim(s)
    last = s.find(" ")
    return s[0:last]

# last name function return last name from string s
def LastName(s):
    s = trim(s)
    first = s.rfind(" ")
    return s[first + 1:len(s)]

# middle name function return middle name from string s
def MiddleName(s):
    s = trim(s)
    first = s.find(" ")
    last = s.rfind(" ")
    return s[first + 1: last]

# main function to perform the file reading and printing 
def main():

    # opening the file named Names.txt in read mode
    file = open('Names.txt', 'r')

    # read all lines of file
    names = file.readlines()

    # printing statememts in formatted manner
    print("{:<10} {:<10} {:<10}".format("First", "Middle", "Last"))
    print("{:<10} {:<10} {:<10}".format("----------", "----------", "----------"))

    # iterating names list one nby one
    for name in names:

        # first remove new line
        name = RemoveNewLine(name)

        # then trim the name
        name = trim(name)

        # then finding first, middle, and last name
        firstName = FirstName(name)
        middleName = MiddleName(name)
        lastName = LastName(name)

        # proper casing of names
        firstName = ProperCase(firstName)
        middleName = ProperCase(middleName)
        lastName = ProperCase(lastName)

        # printing statement
        print("{:<10} {:<10} {:<10}".format(firstName, middleName, lastName))


# calling main function   
main()
