# Python Program to Demonstrate Various Types of Methods

print("M.Sc. Cybersecurity Semester 1")
print("Enrollment No.: 92600565001")
print("Durganand Diwakar")


class Student:

    def instance_method(self):
        print("This is an instance method")

    @classmethod
    def class_method(cls):
        print("This is a class method")

    @staticmethod
    def static_method():
        print("This is a static method")


s = Student()

s.instance_method()
Student.class_method()
Student.static_method()