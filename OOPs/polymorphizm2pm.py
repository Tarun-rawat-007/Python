class Animal():
    def sound(self):
        pass

class Dog(Animal):
    def sound(self):
        print("bhow")

class Cat(Animal):
    def sound(self):
        print("meow")

d=Dog()
c=Cat()

d.sound()
c.sound()


