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