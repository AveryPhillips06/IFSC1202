
def nthOccur(string , ch, N) :
	occur = 0;
	for i in range(len(string)) :
		if (string[i] == ch) : 
			occur += 1;       
		if (occur == N) :   
			return i;
	return -1   	
def occurrence(string , ch) :
	c = 0;
	for i in range(len(string)) :
		if (string[i] == ch) :   
			c += 1;             
	return c	
string = input("Enter the string: "); 
ch = 'f'; 
N = 2; 
if(nthOccur(string, ch, 2) != -1): 
    print(nthOccur(string, ch, 2)) 
elif(occurrence(string,ch)==1):
	  print("One f")
elif(occurrence(string,ch)==0):  
	 print("Zero f")		