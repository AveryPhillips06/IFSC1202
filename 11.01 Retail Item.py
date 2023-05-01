
class RetailItem
{
	String description;
	int units;
	double price;
	RetailItem(String d, int u, double p)
	{
		description = d;
		units = u;
		price = p;
	}
	public void display()
	{
		System.out.println(description+"\t"+units+"\t"+price);
	}
	public static void main(String args[])
	{
		RetailItem item1 = new RetailItem("Jacket",12,59.95);
		RetailItem item2 = new RetailItem("Designer Jeans",40,34.95);
		RetailItem item3 = new RetailItem("Shirt",20,24.95);
		item1.display();
		item2.display();
		item3.display();
	}
}





