# Write a python program to find the factorial of a number.

print("M.Sc.(CS&CL) Semester 1")
print("Enrollment No.: 92600565001")
print("Durganand diwakar")

num = int(input("Enter the number to find the factorial:" ))

fact = 1

for i in range(1,num-1):
    fact = fact * i

print(f"The factorial of the number {num} is {fact}")