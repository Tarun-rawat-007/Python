import pandas as pd


data = {
    'Department': ['HR', 'HR', 'IT', 'IT', 'Finance', 'Finance'],
    'Employee': ['Alice', 'Bob', 'Charlie', 'David', 'Eva', 'Frank'],
    'Salary': [70000, 80000, 90000, 85000, 60000, 75000]
}

df = pd.DataFrame(data)

print("Original DataFrame:")
print(df)


print("\nGrouping by Department and calculating Average Salary by Department:")
average_salary = df.groupby('Department')['Salary'].mean()
print(average_salary)


print("\nSalary Summary by Department:")
salary_summary = df.groupby('Department')['Salary'].agg(['mean', 'sum', 'count'])
print(salary_summary)


print("\nDataFrame Sorted by Salary (Descending):")
sorted_df = df.sort_values(by='Salary', ascending=False)
print(sorted_df)


print("\nDataFrame Sorted by Department and then Salary:")
sorted_multiple = df.sort_values(by=['Department', 'Salary'])
print(sorted_multiple)


print("\nAdding a rank column based on Highest Salary")
df['Rank'] = df['Salary'].rank(ascending=False)
print(df)



