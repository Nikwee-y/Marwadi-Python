class A:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def show(self):
        print("Name is:",self.name)
        print("Age is:",self.age)

obj1=A("Diwuu",21)
obj1.show()