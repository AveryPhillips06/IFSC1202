
class VendingItem(object):
    
    def __init__(self, Name, InitialCount, CostPerItem):
        self.Name = Name
        self.InitialCount = InitialCount
        self.CostPerItem = CostPerItem
        self.SoldCount = 0
        self.LostCount = 0

    def InitialValue(self):
        return self.InitialCount * self.CostPerItem

    def SoldValue(self):
        return self.SoldCount * self.CostPerItem

    def LostValue(self):
        return self.LostCount * self.CostPerItem



class VendingList:
    
    def __init__(self, Name):
        self.Name = Name
        self.Vendinglist = []

        self.VendingTotalInitialValue = 0
        self.VendingTotalInitialCount = 0

        self.VendingTotalSoldValue = 0
        self.VendingTotalSoldCount = 0
        self.VendingTotalLostValue = 0
        self.VendingTotalLostCount = 0

   
    def load_vending_items_from_file(self, filename):
        input1 = open("Final Project Vending.txt," "r")
        ListofLines = input1.readlines()
        input1.close()
        for line in ListofLines:
            tmplist = line.split()
            
            v1 = VendingItem(tmplist[0], int(tmplist[1]), float(tmplist[2]))
            self.VendingTotalInitialValue += v1.InitialValue()
            self.VendingTotalInitialCount += v1.InitialCount
            self.Vendinglist.insert(len(self.Vendinglist), v1)

    
    def print_vending(self):
        print('\tInitial\tPrice\tInitial\tSold\tSold\tLost\tLost')
        print('Product\tCount\tPerItem\tValue\tCount\tValue\tCount\tValue\n')
        for item in self.Vendinglist:
            print("%s\t%d\t%0.2f\t%0.2f\t%d\t%0.2f\t%d\t%0.2f" % (item.Name, item.InitialCount, item.CostPerItem,
                  item.InitialValue(), item.SoldCount, item.SoldValue(), item.LostCount, item.LostValue()))
        print("\n%s\t%d\t%s\t%0.2f\t%d\t%0.2f\t%d\t%0.2f" % ("Total", self.VendingTotalInitialCount, "", self.VendingTotalInitialValue,
              self.VendingTotalSoldCount, self.VendingTotalSoldValue, self.VendingTotalLostCount, self.VendingTotalLostValue))

    def find_product(self, producttofind):
        index = -1
        for item in self.Vendinglist:
            index = index+1
            if item.Name == producttofind:
                return index
        return index

   
    def update_vending(self, productname):
        index = self.find_product(productname)
        if index != -1:
            item = self.Vendinglist[index]
            if item.SoldCount < item.InitialCount:
                item.SoldCount = item.SoldCount+1
                self.VendingTotalSoldCount = self.VendingTotalSoldCount+1
                self.VendingTotalSoldValue = self.VendingTotalSoldValue+item.CostPerItem
            else:
                item.LostCount = item.LostCount+1
                self.VendingTotalLostCount = self.VendingTotalLostCount+1
                self.VendingTotalLostValue = self.VendingTotalLostValue+item.CostPerItem


if __name__ == "__main__":
    list1 = VendingList("drinks")
    list1.load_vending_items_from_file("Final Project Vending.txt")
    input1 = open("Final Project Sales.txt", "r")
    ListofLines = input1.readlines()
    input1.close()
    for line in ListofLines:
        line = line.strip()
        list1.update_vending(line)
    list1.print_vending()