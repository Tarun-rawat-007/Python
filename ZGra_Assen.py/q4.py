class Employee:
    total_salary_paid = 0

    def __init__(self, name, wage, hours):
        self.salary = wage * hours
        Employee.total_salary_paid += self.salary

    @classmethod
    def total_salary(cls):
        return cls.total_salary_paid

    @staticmethod
    def is_eligible_for_overtime(hours):
        return hours > 40


e1 = Employee("Alice", 20, 35)
e2 = Employee("Bob", 25, 45)

print("Alice's and Bob's salary:",e1.salary, e2.salary)  
print("Check overtime eligibility:",Employee.is_eligible_for_overtime(45))  
print("Output total salary paid across employees:",Employee.total_salary())  
