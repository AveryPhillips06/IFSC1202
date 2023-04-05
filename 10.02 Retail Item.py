class Retailltem ():
    def __init__ (self, Description, UnitsOnHand, Price):
        self.Description = Description
        self.UnitsOnHand = UnitsOnHand
        self.Price = Price

inventoryfile = open(" 10.02 Inventory.txt")
x = inventoryfile.readline()
y = x.split(",")
Ratailltem1 = Ratailltem(y[0],y[1],int(y[2]))
x = inventoryfile.readline()
y = x.split(",")
Ratailltem2 = Ratailltem(y[0],y[1],int(y[2]))
print (pet2.Name)
x = inventoryfile.readline()
y = x.split(",")
Ratailltem3 = Ratailltem(y[0],y[1],int(y[2]))
inventoryfile.close()
print("{:<10} {:<10} {:<10}".format("Description", "UnitsOnHand", "Price"))
print("{:<10} {:<10} {:<10}".format(Ratailltem1.Description, Ratailltem1.UnitsOnHand, Ratailltem1.Price))
print("{:<10} {:<10} {:<10}".format(Ratailltem2.Description, Ratailltem2.UnitsOnHand, Ratailltem2.Price))
print("{:<10} {:<10} {:<10}".format(Ratailltem3.Description, Ratailltem3.UnitsOnHand, Ratailltem3.Price))