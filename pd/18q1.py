import pandas as pd

# pd.read_csv(file_path) reads the CSV file into a DataFrame.
df = pd.read_csv('employee_data.csv')
# df.set_index('Employee ID', inplace=True) sets the column 'Employee ID' as the index.
df.set_index('Employee ID', inplace=True)
# inplace=True ensures that the changes are made directly to the DataFrame without creating a new one.
print(df)























# df.set_index('Employee ID')