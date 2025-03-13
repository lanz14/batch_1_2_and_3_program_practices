# Prog05: Create a program that ask user to input a number, continue asking until the user input is invalid. Display the average.

# empty list
numbers = []

# user input
while True:
    user_input = input("(Any non-numeric values will make the program terminate) Input a number: ")


    try:
        number = float(user_input)
        numbers.append(number)
    except ValueError:
        break

# sum all the inputs
    # divide it by the times of inputs
if numbers:
    average = sum(numbers) / len(numbers)

# print the average
    print(f"The average is: {average}")

else:
    print("No valid numbers were entered.")
