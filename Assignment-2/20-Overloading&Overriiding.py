# Python Program to Show Method Overloading and Method Overriding

print("M.Sc.(CS&CL) Semester 1")
print("Enrollment No.: 92600565001")
print("Durganand diwakar")
# Method Overloading

class Calculator:
    def add(self, a=0, b=0, c=0):
        return a + b + c

calc = Calculator()

print("Method Overloading:")
print("Addition of 2 numbers:", calc.add(10, 20))
print("Addition of 3 numbers:", calc.add(10, 20, 30))


# Method Overriding

class Animal:
    def sound(self):
        print("Animal makes a sound")

class Dog(Animal):

    def sound(self):
        print("Dog barks")

animal = Animal()
dog = Dog()

print("\nMethod Overriding:")
animal.sound()
dog.sound()