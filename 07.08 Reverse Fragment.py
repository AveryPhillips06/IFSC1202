
string = input("Enter a string: ")
h_index = [i for i in range(len(string)) if string[i] == 'h']
h_0, h_1 = h_index[0], h_index[-1]
print(string[h_0:h_1+1][::-1])