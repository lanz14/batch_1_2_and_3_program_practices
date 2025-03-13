# Prog03: Create a program that ask user to input a number, continue asking until the user input is invalid. Display "Unique" after input when the inputted number don't have duplicate. Display "Duplicate" after input when the inputted number have duplicate.

# Empty list
previous_inputs = []

# Asking the user to input numbers
print("\nInput any numbers:")

while True:
    user_input = float(input("Input a number: "))

# Check if the input is a "Duplicate" or "Unique" upon inputting
# Terminate the program if the input is invalid