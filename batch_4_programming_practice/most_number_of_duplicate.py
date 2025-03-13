# Prog02: Create a program that ask user to input a number, continue asking until the user input is invalid. Display the number with the most number of duplicate.

# empty set
number_counts = {}

# ask the user to input a number
while True:
    try:
        inputs = int(input("Input a number: "))
        number_counts[inputs] = number_counts.get(inputs, 0) + 1

    except ValueError:
        break 

# check what is the most entered number and print the result
if number_counts:
    most_duplication = max(number_counts, key=number_counts.get)
    print(f"Number with the most number of duplication: {most_duplication} (inputted {number_counts[most_duplication]} times)")

else:
    print("There is no numeric values were inputted.")