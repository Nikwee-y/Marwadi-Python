# Enrollment No: 92600565001

f = open("demo.txt", "w")
f.write("Hello Python")
f.close()

f = open("demo.txt", "r")
print(f.read())
f.close()