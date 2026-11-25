# Python Program to Demonstrate the Use of Methods

print("M.Sc. Cybersecurity Semester 1")
print("Enrollment No.: 92600565001")
print("Durganand Diwakar")

class Calculator:
    def add(self, a, b):
        return a + b

    def multiply(self, a, b):
        return a * b

c = Calculator()

print("Addition:", c.add(10, 5))
print("Multiplication:", c.multiply(10, 5))