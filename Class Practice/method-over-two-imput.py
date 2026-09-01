class Addition:
    def add(self, a, b, c=6)  :
        return a+b+c

obj = Addition()

a = int(input("Enter the number: "))
b = int(input("\nEnter the another number: "))
print("Sum of the two numbers: ",obj.add(a,b))

c= int(input("Enter the value of c: "))
print("Sum of the three numbers: ",obj.add(a,b,c))