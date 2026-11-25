# Write a python program to perform various operations on strings using functions.

print("M.Sc.(CS&CL) Semester 1")
print("Enrollment No.: 92600565001")
print("Durganand diwakar")

def string_operations(text):
    print("Original string:", text)
    print("Length:", len(text))
    print("Uppercase:", text.upper())
    print("Lowercase:", text.lower())
    print("Replace:", text.replace("Python", "Java"))
    print("First character:", text[0])
    print("Last character:", text[-1])


text = "Python Programming"

string_operations(text)