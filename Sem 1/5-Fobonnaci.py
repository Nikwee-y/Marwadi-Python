a,b = 0,1

n = int(input("Enter the number to find the finonnaci series."))

for _ in range(n):
    a,b = b, a+b
    print(a, end=" ")