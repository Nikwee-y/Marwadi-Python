try:
    number = int(input("Enter a number: "))
    print("You entered:",number)
except ValueError:
    print("Error: Invalid input. Please input a number.")