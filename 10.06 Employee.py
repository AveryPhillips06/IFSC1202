class Employee:
   
    
    def __init__(self, FirstName, LastName, IDNumber, HoursWorked, Wage):
        self.FirstName = FirstName
        self.LastName = LastName
        self.IDNumber = IDNumber
        self.HoursWorked = HoursWorked
        self.Wage = Wage
    
    
    def WeeklyPay(self):
        if self.HoursWorked <=  40:
            totalPay = self.HoursWorked * self.Wage
        else:
            basicPay = self.Wage * 40
            overTime = (self.HoursWorked - 40) * self.Wage * 1.5
            totalPay = basicPay + overTime
        return totalPay


data_file = open("10.06 Payroll.txt")


print(f"{'First':>5}{'Last':>8}{'ID':>8}{'Hours':>8}{'Hourly':>8}{'Weekly':>8}")
print(f"{'Name':>5}{'Name':>8}{'Number':>8}{'Worked':>8}{'Wage':>8}{'Pay':>8}")


for line in data_file:

   
    line = line.strip()
    
    if line != '':

        
        line = line.split(', ')

       
        firstName = line[0]
        lastName = line[1]
        idNumber = line[2]
        hoursWorked = float(line[3])
        wage = float(line[4])

        emp = Employee(firstName, lastName, idNumber, hoursWorked, wage)

        fName = emp.FirstName
        lName = emp.LastName
        idNum = emp.IDNumber
        hours = emp.HoursWorked
        wage = emp.Wage

        pay = emp.WeeklyPay()
        
        print(f"{fName:>5}{lName:>8}{idNum:>8}{hours:>8.2f}{wage:>8.2f}{pay:>8.2f}")

data_file.close()