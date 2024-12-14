class Vehicle:
    def __init__(self, brand):
        self.brand = brand  # Set the brand based on the argument

class Car(Vehicle):
    def __init__(self, brand, model):
        super().__init__(brand)  # Pass brand to the parent class
        self.model = model       # Set model in the child class

mycar = Car("toyota", "m6")
print(mycar.brand)  # toyota
print(mycar.model)  # m6

