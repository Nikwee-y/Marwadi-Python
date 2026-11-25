# Enrollment No: 92600565001

f = open("demo.txt", "w")
f.write("Python is a programming language.\n")
f.close()

f = open("demo.txt", "a")
f.write("Programming language.")
f.close()

f = open("demo.txt", "r")
print(f.read())
f.close()