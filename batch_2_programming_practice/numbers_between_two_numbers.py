# Prog10: Create a program that ask user to input 2 numbers. Print all the numbers between the two numbers.

# Input two numbers
number_1 = float(input("Enter the first number: "))
number_2 = float(input("Enter the second number: "))

# What is smaller and bigger number
start = min(number_1, number_2)
end = max(number_1, number_2)

# Printing numbers between the two numbers
current_number = start + 0.1

print(f"Numbers between {start} and {end}:")
while current_number < end: # When reaching the end of the last number, it will end
    print(f"{current_number:.1f}")
    current_number += 0.1