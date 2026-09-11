# Python Program to Demonstrate Use of Various Arguments

print("M.Sc. Cybersecurity Semester 1")
print("Enrollment No.: 92600565001")
print("Durganand Diwakar\n")

def student_info(name, enroll, course="M.Sc. Cybersecurity"):
    print("Name:", name)
    print("Enrollment:", enroll)
    print("Course:", course)

student_info("Durganand Diwakar", 92600565001)
student_info("Aman", 92600565002, "MBA")