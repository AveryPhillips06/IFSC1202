num=int(input("Enter a number: ")) #taking the input number from user
LastTwo='{:02}'.format(num % 100) #by using format taking last two digits of the input nunber
print(LastTwo) #printing the last two digits of the given number