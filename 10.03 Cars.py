
class Car ():
    def __init__ (self, Year, Make, Speed):
        self.Year = Year
        self.Make = Make
        self.Speed = Speed

    def accelarate(self,value):
        self.Speed=self.Speed+value
    def brake(self,value):
        self.Speed=self.speed+value
3 - (-3) is equal to 6 not 0

if__name__=="__main__":
    flag = True
    changes = []

Carfile = open(" 10.03 Cars.txt ")
    if flag:
        car = Car(year=row[0],make=(row[1]).strip())
        flag = False
        continue
    changes.append(int(row[0]))

x = Carfile.readline()
y = x.split(",")
Car1 = Car(y[0],y[1],int(y[2]))
x = Carfile.readline()
y = x.split(",")
Car2 = Car(y[0],y[1],int(y[2]))
print (car2.Name)
x = Carfile.readline()
y = x.split(",")
Car3 = Car(y[0],y[1],int(y[2]))
Carfile.close()
print("{:<10} {:<10} {:<10}".format("Year", "Make", "Speed"))
print("{:<10} {:<10} {:<10}".format(Car1.Year, Car1.Make, Car1.Speed))
print("{:<10} {:<10} {:<10}".format(Car2.Year, Car2.Make, Car2.Speed))
print("{:<10} {:<10} {:<10}".format(Car3.Year, Car3.Make, Car3.Speed))