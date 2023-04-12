class Employee:
    # create class initializer(constructor) 
    def __init__(self, FirstName= "", LastName="", IDNumber = 0, HoursWorked=0, Wage=0):
        # initialize class variables by values passed through constructor 
        self.FirstName = FirstName
        self.LastName = LastName
        self.IDNumber = IDNumber
        self.HoursWorked = HoursWorked
        self.Wage = Wage 

    # define method WeeklyPay() to calculate weekly pay
    def WeeklyPay(self):
        weekly_pay = 0
        # wage is 1 times the wage for 0-40 hours 
        if(self.HoursWorked<=40):
            weekly_pay = self.HoursWorked*self.Wage
        else: 
        # wage is 1 times the wage for 0 - 40 hours and 1.5 time wage for greater than 40 hours 
            weekly_pay = (self.Wage*40)+(self.Wage*1.5*(self.HoursWorked-40))
        return weekly_pay

    ## define __str__ method to print object details
    def __str__(self):
        return self.FirstName+" "+self.LastName+" "+str(self.IDNumber)+" "+str(self.HoursWorked)+" "+str(self.Wage)+" "+str(self.WeeklyPay())

        
## create main function to implement all functionality
if "__main__"== __name__:
    # create file pointer to read file 10.06 Payroll.txt
    file = open("10.06 Payroll.txt")
    # read file line by line 
    # print heading of output
    print("First\tLast\tId\tHours\tHourly\tWeekly")
    print("Name\tName\tNumber\tWorked\tWage\tPay")
    for line in file.readlines():
        line = line.split(",")
        # create Employee class object based details read from file
        emp = Employee(line[0], line[1], int(line[2]), int(line[3]), float(line[4]))
        # print the employee details with weekly pay
        print("{}\t{}\t{}\t{}\t{}\t{:.2f}".format(emp.FirstName, emp.LastName, emp.IDNumber, emp.HoursWorked, emp.Wage, emp.WeeklyPay()))
