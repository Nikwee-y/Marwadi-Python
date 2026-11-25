# Python Program to Demonstrate the Use of Class

print("M.Sc. Cybersecurity Semester 1")
print("Enrollment No.: 92600565001")
print("Durganand Diwakar\n")

class Student:

    def display(self, name, enroll):
        self.name = name
        self.enroll = enroll
        print("Name:", self.name)
        print("Enrollment:", self.enroll)
        print("Course: M.Sc. Cybersecurity")

s1 = Student()
s1.display("Durganand Diwakar", 92600565001)