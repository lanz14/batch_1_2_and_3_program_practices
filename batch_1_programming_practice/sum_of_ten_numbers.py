# Prog07: Create a program that ask user to input 10 numbers. Print the sum of all the numbers.

# Implementing a for loop function in the range of 10
    # Asking the user to input ten numbers
# After obtaining the inputs get the sum

total = 0

for numbers in range(10):
    inputs = float(input(f"Input number {numbers+1}: "))
    total += inputs

print("The sum of all numbers is:", total)