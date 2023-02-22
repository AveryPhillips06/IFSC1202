
f1 = open("06.05 CompareFileA.txt")
f2 = open("06.05 CompareFileB.txt")
lst1 = [] 
lst2 = []
for l in f1:
    lst1.append(l)
    
for l in f2:
    lst2.append(l)
    
cnt=0 #counter
for i in range(len(lst1)):
    if(lst1[i]!=lst2[i]):
        print(f"Line :{i+1} - {lst1[i]}")
        print(f"Line :{i+1} - {lst2[i]}")
        cnt+=1
        
print(cnt,"differences")
    
f1.close()
f2.close()