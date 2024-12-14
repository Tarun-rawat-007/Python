import pandas as pd


file_path = 'employee_data.csv'
df = pd.read_csv(file_path)


mean_salary_by_department = df.groupby('Department')['Salary'].mean()
print(mean_salary_by_department)
