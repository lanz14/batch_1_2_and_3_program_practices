# Prog01: Create a program that ask user to input 2 numbers. Print the smaller number.

# User input of two numbers
    # Displaying a text that the input must be integers only
# elif statements:
    # if number 1 is greater than number 2, print the smaller number is number 2.
    # elif, number 1 is equal to number 2, print they are equal.
    # else, print the smaller number is number 1.

print("\n(For inputs, integers are only acceptable)")

number_1 = int(input("\nInput the first number: "))
number_2 = int(input("Input the second number: "))

if number_1 > number_2:
    print(f"\nThe smaller number is {number_2}")

elif number_1 == number_2:
    print(f"\nThe 2 numbers are the same")

else:
    print(f"\nThe smaller number is {number_1}")