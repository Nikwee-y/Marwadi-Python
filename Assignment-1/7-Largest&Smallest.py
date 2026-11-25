# Write a python program to print the largest element and smallest element in an array.

print("M.Sc.(CS&CL) Semester 1")
print("Enrollment No.: 92600565001")
print("Durganand diwakar")

number = [23,56,87,44,32,66,78,9,34,89,9,45,67]

largest = number[0]
smallest = number[0]

for num in number:
    if num > largest:
        largest = num

    if num < smallest:
        smallest = num

print("The largest number in array is:",largest)
print("The smallest number is:",smallest)