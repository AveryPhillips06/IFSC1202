# Function to find the nth occurrence of a character
def nthOccur(string , ch, N) :
	occur = 0;
	#loop to find nth occurrence of a character
	for i in range(len(string)) :
		if (string[i] == ch) :  #if a character matches the given character
			occur += 1;        #increment the occurrence of the character by 1

		if (occur == N) :   #if the occurrence hits 2 then return its index
			return i;
	
	return -1   

# Function to find the occurrences of a character	
def occurrence(string , ch) :
	c = 0;
	for i in range(len(string)) : #loop to find the occurence of the given character
		if (string[i] == ch) :    #if the character is present in string
			c += 1;              #increment the occurence count by 1 

	return c	#return the count of occurrences of the character
	
string = input("Enter the string: "); #input of the string by user
ch = 'f';  #character whose occurrence needs to be found in string
N = 2;     #we need to find the 2nd occurrence of "f" thus N=2

#if the function call doesn't returns -1 i.e. it returns the index of 2nd occurrence of "f"
if(nthOccur(string, ch, 2) != -1): 
    print(nthOccur(string, ch, 2))  #print the index of 2nd occurrence of "f"
	    
elif(occurrence(string,ch)==1):  # if the function call returns 1 then only 1 "f" occurs in the string
	  print("One f")
	    
elif(occurrence(string,ch)==0):   # if the function call returns 0 then no "f" occurs in the string
	 print("Zero f")		