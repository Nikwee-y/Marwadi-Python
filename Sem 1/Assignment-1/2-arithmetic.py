# Write a python program to do aritmetical operations.

print("M.Sc.(CS&CL) Semester 1")
print("Enrollment No.: 92600565001")
print("Durganand diwakar")

print("Welcome to the Python Calculator.")

print("Please select the operation from the down below.\n" \
"1. Sum\n" \
"2. Substraction\n" \
"3. Multiplication\n" \
"4. Division\n" \
"5. Modulus\n" \
"6. floor division\n" \
"7. Power\n" \
"8. print all operations.")

choose = int(input("Enter the operation number: "))

num1 = int(input('Enter the first number '))
num2 = int(input('Enter the second number: '))

if choose== 1:
    print("The addition of num1 & num2 is:",num1+num2)
elif choose == 2:
    print("The substraction of num1 & num2 is:",num1-num2)
elif choose == 3:
    print("The multiplication of num1 & num2 is:",num1*num2)
elif choose == 4:
    print("The Division of num1 & num2 is:",num1/num2)
elif choose == 5:
    print("The Modulus of num1 & num2 is:",num1%num2)
elif choose == 6:
    print("The Floor Division of num1 & num2 is:",num1//num2)
elif choose == 7:
    print("The Power of num1 & num2 is:",num1**num2)
elif choose == 8:
    print("The addition of num1 & num2 is:",num1+num2,
          "\nThe substraction of num1 & num2 is:",num1-num2,
          "\nThe multiplication of num1 & num2 is:",num1*num2,
          "\nThe Division of num1 & num2 is:",num1/num2,
          "\nThe Modulus of num1 & num2 is:",num1%num2,
          "\nThe Floor Division of num1 & num2 is:",num1//num2,
          "\nThe Power of num1 & num2 is:",num1**num2
          )
else:
    print("Please choose a correct number from the above listed one")