class RetailItem:
    def __init__(self, description="", units_on_hand=0, price=0):
        self.description = description
        self.units_on_hand = units_on_hand
        self.price = price

    def inventory_value(self):
        return self.units_on_hand * self.price

# Read the inventory file
with open("10.02 Inventory.txt", "r") as f:
    lines = f.readlines()

# Create RetailItem objects for each line in the file
items = []
for line in lines:
    data = line.strip().split(", ")
    item = RetailItem(description=data[0], units_on_hand=int(data[1]), price=float(data[2]))
    items.append(item)
# Generate and print the report
print("{:<10} {:<15} {:<10} {}".format("Description", "Units On Hand", "Price", "Inventory Value"))
for item in items:
    print("{:<10} {:<15} {:<10.2f} {:.2f}".format(item.description, item.units_on_hand, item.price, item.inventory_value()))