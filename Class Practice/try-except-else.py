try:
    attempts = int(input("Enter number of login attempts: "))

except ValueError:
    print("Invalid input. Please enter a number")

else:
    print("Login attempts recorded:",attempts)