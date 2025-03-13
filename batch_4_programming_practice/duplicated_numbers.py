# Prog01: Create a program that ask user to input 10 numbers. Display all numbers that have duplicate.

# empty sets
numbers = []
duplicates = set()

# user input
for i in range(10):
    num = int(input(f"Enter number {i+1}: "))

# check if there is a duplication
    if num in numbers:
        duplicates.add(num)
    numbers.append(num) 

# display duplicates
if duplicates:
    print("Duplicate numbers:", duplicates)
else:
    print("No duplicate numbers found.")