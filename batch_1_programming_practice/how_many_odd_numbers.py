# Prog08: Create a program that ask user to input 10 numbers. Print how many are odd numbers.

# Ask the user to input ten numbers
    # Adding a warning text to input integers only
# If a number input is not equal to a remainder of zero it will be added as an odd number
# Printing how many are the odd numbers
# Indicating what odd numbers were entered

print("(Integers are only acceptable inputs)")

for input in range(10):
    numbers = int(input(f"Input number {input+1}: "))