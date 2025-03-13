# Prog01: Create a program that ask user to input 10 numbers. Display all numbers that don't have duplicate.

# Asking user to input ten numbers
print("Input 10 numbers:")

for inputs in range(10):
    number = float(input(f"Enter number {inputs+1}: "))

# Identify numbers that have no duplicates
# Print result