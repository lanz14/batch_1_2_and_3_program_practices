# Prog04: Create a program that ask user to input 2 numbers. Print the quotient of the two numbers without the decimal point

import math

# Warning text
print("\n(For inputs, integers are only acceptable)")

# User input
number_1 = int(input("\nInput the first number: "))
number_2 = int(input("Input the second number: "))

# Get the quotient
quotient = number_1 / number_2

# Rounding up
decimal = quotient % 1

# Print result without decimal point
if decimal >= 0.5:
    rounded_up = math.ceil(quotient)
    print(f"\nThe quotient is {quotient} rounded up to {rounded_up}")

elif 0.1 <= decimal <= 0.4:
    rounded = math.floor(quotient)
    print(f"\nThe quotient is {quotient} rounded to {rounded}")

else:
    print(f"\nThe quotient is: {int(quotient)}")