class Car:
    def __init__(self):
        self.__price = 15000  # Private attribute to store the car's price

    def sell(self):
        print("Selling Price:",self.__price)

    def set_price(self, price):
        if price > 0:
            self.__price = price  


c = Car()
c.sell()  # Selling Price: $15000

# Attempt to change the price directly (won't affect the private attribute)
c.__price = 20000
c.sell()  # Selling Price: $15000

# Using the setter method to change the price
c.set_price(20000)
c.sell()  # Selling Price: $20000

