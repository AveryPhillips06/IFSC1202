# Prompt for input
input_str = input("Enter Values Separated by Spaces: ")

# Split input string into a list of strings
input_list = input_str.split()

# Convert list of strings to list of integers
int_list = []
for i in range(len(input_list)):
    int_list.append(int(input_list[i]))

# Print values with odd index number
for i in range(1, len(int_list), 2):
    print(int_list[i])
