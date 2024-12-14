class Car:
    def __init__(self,brand,model):
        self.__brand=brand
        self.__model=model

    def set_brand(self,brand):
        self.__brand=brand

    def set_model(self,model):
        self.__model=model

    def get_brand(self):
        return self.__brand
    
    def  get_model(self):
        return self.__model
    

car = Car("Toyota", "Corolla")
print(car.get_brand())  # Toyota
print(car.get_model())  # Corolla

# set method to change its private variable 
car.set_brand("Honda")
car.set_model("Civic")

print(car.get_brand())  # Honda
print(car.get_model())  # Civic

