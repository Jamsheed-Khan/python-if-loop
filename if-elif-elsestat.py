# Problem-1: Conditionals (if-elif-else)
# Write a Python program that takes an integer as input from the user.
# If the integer is even, print "The number is even. "
# If the integer is odd, print "The number is odd."
# If the input is not an integer, print "Invalid input, please enter an integer."
Userinput = input('Enter a Number : ')
if Userinput.isdigit():
    number = int(Userinput)
    if number % 2 == 0:
        print('The Number is Even.')
    else:
        print('The Number is Odd.')

else:
    print('Invalid input,please enter an integer ')
