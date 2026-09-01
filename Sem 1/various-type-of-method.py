# Write a python program to demonstrate the use of methods

class Student:
    # Methos to display student details.
    def display_details(self,name,enrollment_no,department):
        print("University: Marwadi University")
        print("Student name:",name)
        print("Enrollment no:",enrollment_no)
        print("Department:",department)

    # Method to calculate total marks
    def calculate_marks(self,marks1,marks2,marks3):
        total = marks1 + marks2 + marks3
        return total

# Creating an object of class
Student = Student() 

# Calling the display details 
Student.display_details(
    "Mansi chudail",
    "MU56093405001",
    "Student of msc cybersecurity"
)

@classmethod
def display_university(cls):
    print("University:",cls.university)

@staticmethod
def check_result(marks):
    if marks > 40:
        return "Pass"
    else:
        return("Fail")


# Calling the calculate_marks() method
total = Student.calculate_marks(34,67,90)

print("Total marks:",total)