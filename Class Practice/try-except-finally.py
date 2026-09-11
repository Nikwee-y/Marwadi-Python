a = 10
b = 2

try:
    attempts = int(input("Invalid input. Please enter a number."))
    print("Login attempts:",attempts)
except ValueError:
    print("Invalid input. Please enter a number.")
finally:
    print("Security check completed.")