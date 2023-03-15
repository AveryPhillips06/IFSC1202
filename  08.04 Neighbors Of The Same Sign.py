num_string = input("Enter Values Separated by Spaces: ")
num_list = [int(num) for num in num_string.split()]
for i in range(len(num_list) - 1):
      if (num_list[i] >= 0 and num_list[i+1] >= 0) or (num_list[i] < 0 and num_list[i+1] < 0):
           print(num_list[i], num_list[i+1])
           break
else:
       print(" ")