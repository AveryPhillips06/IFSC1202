#defining a function
def LeapOrNot(n):
    #checking conditions for leap year
    if n%400==0 or n%100!=0 and n%4==0:
        print("LEAP YEAR")
    else:
        #if not leap year then its a normal year
        print("COMMON YEAR")

#taking user input
n=int(input("Enter year:\n"))
#passing input onto function
LeapOrNot(n)