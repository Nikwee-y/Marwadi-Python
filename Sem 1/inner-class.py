# Write a python program to demonstrate the inner class 

# Outer Class
class College:

    def __init__(self,college_name):
        self.college_name = college_name

    # Inner class
    class Faculty:
        def __init__(self,name,faculty_id,department):
            self.name = name
            self.faculty_id = faculty_id
            self.department = department

        def display(self):
            print("Faculty name:",self.name)
            print("faculty_id:",self.faculty_id)
            print("Department:",self.department)

# Create an object of the outer class
clg = College("Presidency College")

# Create an object of the inner class
fac = clg.Faculty(
    "Mohammad Jeelan",
    "PC1001",
    "Faculty of Computer Application"
)

# Display faculty details
print("College:",clg.college_name)
fac.display()