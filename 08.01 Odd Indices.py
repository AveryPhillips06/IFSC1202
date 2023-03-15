input_str = input("Enter Values Separated by Spaces: ")
input_list = input_str.split()
int_list = []
for i in range(len(input_list)):
    int_list.append(int(input_list[i]))
for i in range(1, len(int_list), 2):
    print(int_list[i])
