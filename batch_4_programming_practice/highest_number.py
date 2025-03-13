# Prog03: Create a program that ask user to input a number, continue asking until the user input is invalid. Display the highest number

highest_number = None

# user input
while True:
    try:
        num = int(input("Input a number: "))
        
# check for the highest input
        if highest_number is None or num > highest_number:
            highest_number = num
            
    except ValueError:
        break

# print the result
if highest_number is not None:
    print(f"\nHighest number: {highest_number}")
else:
    print("No valid numbers were inputted")