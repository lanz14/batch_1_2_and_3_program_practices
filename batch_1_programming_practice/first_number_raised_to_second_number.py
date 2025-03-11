# Prog06: Create a program that ask user to input 2 numbers. Print the result when the first number is raised to the second number.

# Ask the user to input two numbers
    # The numbers must be integers only.
# First number raised to the second number
# Print the result

print("(Integers are the only acceptable inputs)")

number_1 = int(input("Input the first number: "))
number_2 = int(input("Input the first number: "))

result = number_1 ** number_2

print(f"{number_1} raised to {number_2} is equal to: {result}")