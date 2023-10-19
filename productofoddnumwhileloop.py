# (d) Write a Python program that calculates
# the product of all odd numbers from 1 to 15 (inclusive)
# using a while loop and prints the result.
num = 1
product = 1
while (num<=15):
    if num % 2 != 0:
        product = product * num
    num = num+1
print("The product of Odd Number is : ")
print(product)
