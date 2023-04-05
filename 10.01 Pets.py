class Pet ():
    def __init__ (self, Name, Type, Age):
        self.Name = Name
        self.Type = Type
        self.Age = Age

petfile = open("10.01 Pets.txt")
x = petfile.readline()
y = x.split(",")
pet1 = Pet(y[0],y[1],int(y[2]))
x = petfile.readline()
y = x.split(",")
pet2 = Pet(y[0],y[1],int(y[2]))
print (pet2.Name)
x = petfile.readline()
y = x.split(",")
pet3 = Pet(y[0],y[1],int(y[2]))
petfile.close()
print("{:<10} {:<10} {:<10}".format("Name", "Type", "Age"))
print("{:<10} {:<10} {:<10}".format(pet1.Name, pet1.Type, pet1.Age))
print("{:<10} {:<10} {:<10}".format(pet2.Name, pet2.Type, pet2.Age))
print("{:<10} {:<10} {:<10}".format(pet3.Name, pet3.Type, pet3.Age))