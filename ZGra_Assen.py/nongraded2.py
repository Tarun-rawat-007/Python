# non graded 2
# Question 1:
# Problem: You are required to implement a multilevel inheritance structure using three classes: Vehicle, Car, and SportsCar. Each class should have a method called description() that returns a string describing the type of vehicle.
# •	The Vehicle class should have a method description() that returns "This is a vehicle."
# •	The Car class should inherit from Vehicle and override the description() method to return "This is a car."
# •	The SportsCar class should inherit from Car and override the description() method to return "This is a sports car."
# You should also print the MRO of the SportsCar class.

class Vehicle:
    def description(self):
        return "This is a vehicle"


class Car(Vehicle):
    def description(self):
        return "This is a car"


class SportsCar(Car):
    def description(self):
        return super().description() 


sports_car = SportsCar()


print(sports_car.description())  


print(SportsCar.__mro__)  
print(SportsCar.mro())  


# Question 2:
# Problem: Create three classes A, B, and C where C inherits from B, and B inherits from A. Class A should contain a method divide() that takes two parameters and performs division. In class A, handle a ZeroDivisionError using a try-except block.
# •	In class A, the method divide(self, x, y) should perform x / y.

# class A:
#     def divide(self, x, y):
#         try:
#             result = x / y
#         except ZeroDivisionError:
#             return "Division by zero is not allowed."
#         else:
#             return f"The result of {x} / {y} is: {result}"

# class B(A):
#     pass

# class C(B):
#     pass

# obj = C()

# print(obj.divide(10, 2))  


# print(obj.divide(10, 0))  
