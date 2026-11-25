# Write a python program to add two matrix using array and functions.

print("M.Sc.(CS&CL) Semester 1")
print("Enrollment No.: 92600565001")
print("Durganand diwakar")

def add_matrix(a, b):
    result = [[0,0,0],[0,0,0],[0,0,0]]
    for i in range(len(a)):
        for j in range(len(a[0])):
            result[i][j] = a[i][j] + b[i][j]
    return result

A = [[1,2,3],[4,5,6],[7,8,9]]
B = [[9,8,7],[6,5,4],[3,2,1]]

print("Matrix A:", A)
print("Matrix B:", B)
print("Sum of matrices:", add_matrix(A,B))