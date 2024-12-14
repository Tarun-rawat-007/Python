class Person:
    def __init__(self,name,age) :
        print("Hi i am a constructor")   # call  itself run everyyitime when object is created constructor
        self.name=name
        self.age=age



a=Person("Tarun",22)
print(a.name,a.age)
