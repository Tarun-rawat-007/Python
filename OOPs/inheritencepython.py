class Animal:
    def says(self):
        print("I am animal")

# derived class
class dog(Animal):
    def saysdog(self):
        print('I am dog')


dog1=dog()    #object of class
dog1.says()
dog1.saysdog()

