
for i in range(len(num_list)-1):
    if (num_list[i] >= 0 and num_list[i+1] >= 0) or (num_list[i] < 0 and num_list[i+1] < 0):
        print(f"The first adjacent elements with the same sign are {num_list[i]} and {num_list[i+1]}.")
        break
else:
    print("There are no adjacent elements with the same sign.")