# Prog06: Create a program that ask user to input 10 numbers. Print the result of the first number minus all of the remaining numbers.

# Create an empty list to store the numbers.
numbers = []

# User input of ten numbers
print("Input ten numbers")
for i in range(10):
    inputs = float(input(f"Input number {i+1}: "))
    numbers.append(inputs)

# Calculating first number minus remaining nine numbers
result = numbers[0]
for i in range(1, 10):
    result -= numbers[i]

# Print result
print(f"The first number minus all remaining numbers is: {result}")