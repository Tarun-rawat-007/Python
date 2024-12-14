class Person:
    def __init__(self, name, age):
        self._name = name  
        self._age = age    

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value


    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        if value >= 0:  
            self._age = value
        else:
            raise ValueError("Age cannot be negative.")


    def is_minor(self):
        return self._age < 18


person = Person("John", 20)
print("name:",person.name)    
print("age:",person.age)      
print("Is Minor:",person.is_minor())


