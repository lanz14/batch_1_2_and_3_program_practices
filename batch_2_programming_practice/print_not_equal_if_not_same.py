# Prog02: Create a program that ask user to input 2 numbers. Print "Not Equal" when the numbers are not the same.

# Adding a warning text that inputs must be in integers only
print("\n(For inputs, integers are only acceptable)")

# User inputs
number_1 = int(input("\nInput the first number: "))
number_2 = int(input("Input the second number: "))

# If number 1 is greater than number 2
if number_1 > number_2:
    # Print "Not Equal"
    print("\nNot Equal")

# If number 1 is less than number 2
elif number_1 < number_2:
    # Print "Not Equal"
    print("\nNot Equal")

# If number 1 is equal to number 2
else:
    # Print that the two numbers are equal
    print("\nThe numbers are the same")