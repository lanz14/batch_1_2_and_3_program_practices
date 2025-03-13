# Prog04: Create a program that ask user to input a number, continue asking until the user input is invalid. Display the number from highest to lowest. Clue: sort() function

# empty list
numbers = []

# user input
while True:
    user_input = input("(Any non-numeric values will make the program terminate) Input a number: ")

    try:
        num = float(user_input)
        numbers.append(num)

    except ValueError:
        print("Invalid input. Program terminated.")
        break

# arrange from highest to lowest
# display the sorted numbers
if numbers:
    numbers.sort(reverse=True)
    
    print("\nSorted from highest to lowest:")
    for num in numbers:
        print(num)
else:
    print("No valid numbers were inputted.")