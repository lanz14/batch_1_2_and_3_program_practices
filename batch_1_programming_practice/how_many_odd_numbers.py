# Prog08: Create a program that ask user to input 10 numbers. Print how many are odd numbers.

# Ask the user to input ten numbers
    # Adding a warning text to input integers only
# If a number input is not equal to a remainder of zero it will be added as an odd number
# Printing how many are the odd numbers
# Indicating what odd numbers were entered

print("(Integers are only acceptable inputs)")

odd_count = 0
odd_numbers = []

for inputs in range(10):
    numbers = int(input(f"Input number {inputs+1}: "))
    if numbers % 2 != 0:
        odd_count += 1
        odd_numbers.append(numbers)

print(f"The number of odd numbers entered is: {odd_count}")

if odd_numbers:
        print("The odd numbers are:", ", ".join(map(str, odd_numbers)))
else:
    pass
