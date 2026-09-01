class Animal:
    def sound(self):
        print('Animal make a sound')

class Dog(Animal):
    def sound(self):
        print("Dog Barks")

a = Animal()
b = Dog()

a.sound()
b.sound()
