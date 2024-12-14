class Animal:
    def says(self):
        print("I am animal")


class Dog(Animal):
    def says(self):
        print("I am dog")


dog1 = Dog()
dog1.says()  # Output: I am dog (method overridden)
