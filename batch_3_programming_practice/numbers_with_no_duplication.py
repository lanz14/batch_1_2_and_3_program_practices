# Prog01: Create a program that ask user to input 10 numbers. Display all numbers that don't have duplicate.

# Asking user to input ten numbers
def main():
    numbers = []

    print("Input 10 numbers:")

    for inputs in range(10):
        while True:
            try:
                number = float(input(f"Input number {inputs+1}: "))
                numbers.append(number)
                break
            except ValueError:
                print("Invalid input. Input a valid number")

# Identify numbers that have no duplicates
    no_duplicate_numbers = []
    for num in numbers:
        if numbers.count(num) == 1:
            no_duplicate_numbers.append(num)

# Print result
    if no_duplicate_numbers:
        print("\nNumbers that don't have duplicates:")
        for num in no_duplicate_numbers:
            print(num)
    else:
        print("\nThere are no numbers without duplicates.")

if __name__ == "__main__":
    main()