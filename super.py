class Animal:
    def sound(self):
        print("Animal sound")

class Dog(Animal):
    def sound(self):
        print("Woof")
        super().sound()  # Call the parent class's sound method


dog = Dog()
dog.sound()     # This will call the Animal's sound  woof then animal method 

