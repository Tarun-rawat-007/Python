import pandas as pd

employee_data = pd.DataFrame({
    'Employee ID': [101, 102, 103, 104, 105],
    'Name': ['John Smith', 'Jane Doe', 'Bob Johnson', 'Alice Brown', 'David Wilson'],
    'Department': ['Engineering', 'Marketing', 'Sales', 'HR', 'Sales'],
    'Position': ['Software Engineer', 'Marketing Manager', 'Sales Executive', 'HR Specialist', 'Sales Manager'],
    'Salary': [80000, 75000, 60000, 65000, 70000],
    'Experience': [4, 6, 7, 5, 8]
})


budget_data = pd.DataFrame({
    'Employee ID': [None] * 4,  
    'Name': [None] * 4,         
    'Department': ['Engineering', 'Marketing', 'Sales', 'HR'],
    'Position': [None] * 4,     
    'Salary': [None] * 4,       
    'Experience': [None] * 4     
})


budget_data['Budget'] = [1500000, 1200000, 1000000, 800000]
concatenated_data = pd.concat([employee_data, budget_data], ignore_index=True)
print(concatenated_data)
