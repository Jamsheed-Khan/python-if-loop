# (c) Write a Python program that calculates
# the sum of all even numbers from 1 to 50 (inclusive)
# using a for loop and prints the result.
Num = 1
sum =0
for num in range(50):
    if num % 2 == 0:
        sum =sum+num
print('The sum of Even number is : ')
print(sum)
