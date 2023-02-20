#open files
f1 = open("CompareFileA.txt")
f2 = open("CompareFileB.txt")
#make lists to store lines
lst1 = [] 
lst2 = []

#store lines 
for l in f1:
    lst1.append(l)
    
for l in f2:
    lst2.append(l)
    
cnt=0 #counter
#loop to compare lines
for i in range(len(lst1)):
    if(lst1[i]!=lst2[i]):
        print(f"Line :{i+1} - {lst1[i]}")
        print(f"Line :{i+1} - {lst2[i]}")
        cnt+=1
        
#print differences
print(cnt,"differences")
    
#close files     
f1.close()
f2.close()