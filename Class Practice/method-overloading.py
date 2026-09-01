class Addition:
    def add(self,a,b,c=0):
        return a+b+c

obj = Addition()

print("The addition of two number is:",obj.add(45,78))
print("The addition of three number's is:",obj.add(45,78,12))
