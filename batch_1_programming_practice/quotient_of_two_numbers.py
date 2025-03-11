# Prog05: Create a program that ask user to input 2 numbers. Print the quotient of the two numbers with the decimal point

# Ask the user to input two numbers
    # Inputs are integers only
# The first number divided by the second number
# Get the quotient and then print the result

print("(For inputs, integers are only acceptable)")

number_1 = int(input("Input the first number: "))
number_2 = int(input("Input the second number: "))

quotient = number_1 / number_2

print("\nThe quotient is: %.2f"%quotient)