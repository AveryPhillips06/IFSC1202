def desks(s):
    if s%2==0:
        return s//2
    else:
        return (s//2)+1



#taking number of students in each class
a=int(input("Students in class A:"))
b=int(input("Students in class B:"))
c=int(input("Students in class C:"))


#calling function
number_of_desks=0
number_of_desks=desks(a)
number_of_desks+=desks(b)
number_of_desks+=desks(c)

#printing function
print(number_of_desks)