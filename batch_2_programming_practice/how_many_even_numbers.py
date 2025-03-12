# Prog07: Create a program that ask user to input 10 numbers. Print how many are even numbers.

# ask the user to input 10 numbers
even_count = 0

for inputs in range(10):
    numbers = int(input(f"Input number {inputs+1}: "))

# if the entered number is equal to a remainder of 0 it will add as even number
    if numbers % 2 == 0:
        even_count += 1

# print the result
print(f"The number of even number/s: {even_count}")