class Person:
    def __init__(self, name, age):
        self.name = name  
        self.age = age    

    def display_info(self):
        print("Name:",self.name)
        print("Age:",self.age)
     
    
class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)  
        self.student_id = student_id 

    def display_info(self):
        super().display_info()  
        print("Student ID: ",self.student_id)


student = Student("Alice", 21, "S12345")
student.display_info()
