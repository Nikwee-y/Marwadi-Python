# Enrollment No: 92600565001

try:
    a = int(input("Enter the number: "))
    b = int(input("Enter the divisor: "))
    print(a/b)
except ZeroDivisionError:
    print("Cannot divide by zero.")