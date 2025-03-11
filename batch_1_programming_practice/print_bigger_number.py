# Prog01: Create a program that ask user to input 2 numbers. Print the bigger number.

# Ask the user to input two numbers
    # Inputs are only integers
# elif statements
    # If the number 1 is greater than number 2, number 1 will be printed.
    # If the number 1 is equal to number 2, the output will be they are both equal.
    # else the number 2 will be printed as the bigger number, if these are false.

print("(Integers are the only acceptable inputs)")

number_1 = int(input("Enter the first number: "))
number_2 = int(input("Enter the second number: "))

if number_1 > number_2:
    print(f"\nThe bigger number is {number_1}")

elif number_1 == number_2:
    print(f"\nThere are no bigger numbers since they are both equal.")

else:
    print(f"\nThe bigger number is {number_2}")