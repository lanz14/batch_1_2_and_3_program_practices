# Prog05: Create a program that ask user to input a number, continue asking until the user input is invalid. Display the number from lowest to highest. Clue: sort() function

# empty list
numbers = []

# user input indicating that any non-numeric will terminate the program
while True:
    user_input = input("(Any non-numeric values will make the program terminate) Input a number: ")

# check if inputs are valid
    try:
        number = float(user_input)
        numbers.append(number)

    except ValueError:  
        break  

# display the sorted numbers
numbers.sort() 
print("\nSorted numbers:", numbers)