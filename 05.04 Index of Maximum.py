highest = 0
index = 0
highest_index =0
while True:
        num = int(input('Enter a Number (zero to quit):'))
        if (num==0): break
        index+=1
        if num>highest:
            highest,highest_index=num,index

print('Maximun:{}'.format (highest))
print ('Index of Maximum: {}'.format(highest_index))