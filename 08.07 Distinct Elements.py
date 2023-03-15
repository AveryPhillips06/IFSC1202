a = input("Enter Values Seperated by Spaces : ")
a_list = a.split()
a_distinct = len(set(a_list))
print("Number of Distinct Elements : ", a_distinct)