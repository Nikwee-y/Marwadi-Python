# Write a python program to print the fibonacci sequence.

print("M.Sc.(CS&CL) Semester 1")
print("Enrollment No.: 92600565001")
print("Durganand diwakar")

a,b = 0,1

n = int(input("Enter the number to find the finonnaci series."))

for _ in range(n):
    a,b = b, a+b
    print(a, end=" ")