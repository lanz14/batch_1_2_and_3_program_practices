# Prog02: Create a program that ask user to input 10 numbers. Display all numbers. For numbers with duplicate, display only the first entry.

# Initializing two empty lists
numbers = []
no_duplicate_numbers = []

# User input (10 numbers)
print("Input 10 numbers:")
for i in range(10):
    num = int(input(f"Number {i+1}: "))
    numbers.append(num)
    if num not in no_duplicate_numbers:
        no_duplicate_numbers.append(num)

# Print the user's input numbers
print(f"\nYour inputs: {numbers}")

# Print the numbers without duplication, keeping the first entry
print(f"\nNumbers without duplication (first entries only): {no_duplicate_numbers}")