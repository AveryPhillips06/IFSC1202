
def LeapOrNot(n):
    if n%400==0 or n%100!=0 and n%4==0:
        print("LEAP YEAR")
    else:
        print("COMMON YEAR")

n=int(input("Enter year:\n"))
LeapOrNot(n)