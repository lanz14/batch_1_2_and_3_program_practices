# Prog09: Create a program that print all the numbers starting from 0 to 100 except numbers ending in zero or ending five.

# iterate range of 1-100
for numbers in range(0,101):

# Check if number is ending with 0 and 5
    if numbers % 5 != 0 and numbers % 10 != 0:

# print result
        print(numbers)