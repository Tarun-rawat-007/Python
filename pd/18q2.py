import pandas as pd

# Load the employee data from a CSV file
file_path = 'employee_data.csv'  # Replace with your CSV file path
df = pd.read_csv(file_path)

# Filter employees from the Sales department with more than 5 years of experience
filtered_df = df[(df['Department'] == 'Sales') & (df['Experience'] > 5)]

# Display the filtered DataFrame
print(filtered_df)

