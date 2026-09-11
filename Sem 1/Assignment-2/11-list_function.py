# Python Program to Demonstrate Use of Dictionary and Various Functions

print("M.Sc. Cybersecurity Semester 1")
print("Enrollment No.: 92600565001")
print("Durganand Diwakar")

my_dict = {"name": "Durganand", "enroll": 92600565001, "course": "M.Sc. Cybersecurity"}

print("Dictionary:", my_dict)
print("Keys:", my_dict.keys())
print("Values:", my_dict.values())
print("Access name:", my_dict["name"])

my_dict["semester"] = 1
print("Updated dictionary:", my_dict)
print("Total items:", len(my_dict))