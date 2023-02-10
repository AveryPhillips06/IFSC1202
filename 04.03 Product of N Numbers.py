n=int(input("Enter n: "))
# sum to store factorial of numbers from 1 to n
sum=0
# store factorial
fact=1
# i will run from 1 t n
for i in range(1,n+1):
  # multiply previously calculated fact with i
  fact=fact*i
  # add ne
  sum=sum+fact
# print sum
print("sum = ",sum)