# Python Program to Demonstrate the Concept of Inner Class

print("M.Sc. Cybersecurity Semester 1")
print("Enrollment No.: 92600565001")
print("Durganand Diwakar")

class Outer:
    def __init__(self):
        print("This is Outer Class")

    class Inner:
        def __init__(self):
            print("This is Inner Class")

        def display(self):
            print("Inner class method")


a1 = Outer()
b = a1.Inner()
b.display()