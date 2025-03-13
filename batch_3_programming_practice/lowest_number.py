# Prog04: Create a program that ask user to input a number, continue asking until the user input is invalid. Display the lowest number

# Empty list
numbers = []
    
while True:
    user_input = (input("(Any non-numeric will quit the program) Input a number: "))

# Check if inputs are valid  
    try:
        inputs = float(user_input)
        numbers.append(user_input)
            
    except ValueError:
        print("That's not a valid number. Program terminated.")
        break

# Display lowest number
if numbers:
    lowest_number = min(numbers)
    print(f"\nThe lowest number you entered: {lowest_number}")
else:
    print("\nNo valid numbers were entered.")
