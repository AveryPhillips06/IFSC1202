s= "abch123h456hdef" //you can use input to take input but i have use predefined strring for help here
a=s.find('h') //this finds if there is any h from begenning indexing from 0
a=a+1 //to increment a with 1 you'll understand why
b=s.rfind('h') // this finds if any h from beckward
if(a==b): //if there is only h or none is there then both index will be same and string need to reverse
print(a) //prints a
else:       
 print(s[:a],end="") this prints upto frist h found
t=s[a:b] //this provide a substring of s from a to b;
print(t[::-1],end="") //this prints given substring t in reverse order (-1)
print(s[b:],end="") //this prints rest of the string
//and you get the required resultn i.e abch654h321hdef

//please don't mess with indentation it will cause issues