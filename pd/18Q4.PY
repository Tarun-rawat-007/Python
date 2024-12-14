import pandas as pd

# Load the employee data from a CSV file
file_path = 'employee_data.csv'  # Replace with your CSV file path
df = pd.read_csv(file_path)

# Sort the DataFrame by Salary in descending order
df_sorted = df.sort_values(by='Salary', ascending=True)

# Add a new column 'Salary Rank' that ranks employees based on their salaries
df_sorted['Salary Rank'] = df_sorted['Salary'].rank(ascending=False)

# Display the updated DataFrame
print(df_sorted)
