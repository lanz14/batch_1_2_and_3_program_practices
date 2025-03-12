# Prog04: Create a program that ask user to input 2 numbers. Print the quotient of the two numbers without the decimal point

import math

# Warning text
print("\n(For inputs, integers are only acceptable)")

# User input
number_1 = int(input("\nInput the first number: "))
number_2 = int(input("Input the second number: "))

# Get the quotient
quotient = number_1 / number_2

# Print result without decimal point
if quotient % 1 > 0:
    rounded_up = math.ceil(quotient)
    print(f"\nThe quotient is {quotient} rounded up to {rounded_up}")
elif quotient % 1 == 0:
        print(f"\nThe quotient is: {int(quotient)}")