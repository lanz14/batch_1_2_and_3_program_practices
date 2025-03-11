# Prog02: Create a program that ask user to input 2 numbers. Print "Equal" when the numbers are the same.

# Ask the user to input 2 numbers
    # print a warning text that integers are the only acceptable inputs
# Create an elif statements:
    # If number 1 is greater than number 2 the output will be "Not Equal"
    # elif number 1 is equal to number 2 the output will be "Equal"
    # else, number 1 is less than number 2 the output will be "Not Equal"

print("(For inputs, integers are only acceptable)")

number_1 = int(input("Input the first number: "))
number_2 = int(input("Input the second number: "))

if number_1 > number_2:
    print("\nNot Equal")

elif number_1 == number_2:
    print("\nEqual")

else:
    print("\nNot Equal")

