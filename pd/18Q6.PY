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
    'Department': ['Engineering', 'Marketing', 'Sales', 'HR'],
    'Budget': [1500000, 1200000, 1000000, 800000]
})

merged_data = pd.merge(employee_data, budget_data, on='Department')
print(merged_data)
