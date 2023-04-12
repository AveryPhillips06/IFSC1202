class Retailltem ():
    def __init__ (self, Description="", UnitsOnHand=0, Price=0):
        self.Description = Description
        self.UnitsOnHand = Units_On_Hand
        self.Price = Price
    def inventory_value(self):
        return self.Units_On_Hand * self.price
with open("10.02 Inventory.txt", "r") as f:
    lines = f.readlines()

    items = []
for line in lines:
    data = line.strip().split(", ")
    item = RetailItem(description=data[0], units_on_hand=int(data[1]), price=float(data[2]))
    items.append(item)

x = inventoryfile.readline()
y = x.split(",")
Ratailltem1 = Ratailltem(y[0],y[1],int(y[2]))
x = inventoryfile.readline()
y = x.split(",")
Ratailltem2 = Ratailltem(y[0],y[1],int(y[2]))
print (Retailltem2.Units_On_Hand)
x = inventoryfile.readline()
y = x.split(",")
Ratailltem3 = Ratailltem(y[0],y[1],int(y[2]))
inventoryfile.close()
print("{:<10} {:<15} {:<10}{}".format("Description", "Units_On_Hand", "Price", Inventory))
print("{:<10} {:<15} {:<10}".format(Ratailltem1.Description, Ratailltem1.Units_On_Hand, Ratailltem1.Price))
print("{:<10} {:<10} {:<10}".format(Ratailltem2.Description, Ratailltem2.Units_On_Hand, Ratailltem2.Price))
print("{:<10} {:<10} {:<10}".format(Ratailltem3.Description, Ratailltem3.Units_On_Hand, Ratailltem3.Price))