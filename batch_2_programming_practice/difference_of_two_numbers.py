# Prog03: Create a program that ask user to input 2 numbers. Print the difference of the two numbers.

# Adding a warning text that inputs must be in integers only
print("\n(For inputs, integers are only acceptable)")

# User input
number_1 = int(input("\nInput the first number: "))
number_2 = int(input("Input the second number: "))

# number 1 minus number 2
difference = number_1 - number_2

# Print the difference
print("\nThe difference is:", difference)