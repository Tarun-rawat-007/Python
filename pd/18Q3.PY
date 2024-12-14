import pandas as pd

# Load the employee data from a CSV file
file_path = 'employee_data.csv'  # Replace with your CSV file path
df = pd.read_csv(file_path)

# Drop rows with missing values in the 'age' column
df_cleaned = df.dropna(subset=['age'])

# Display the cleaned DataFrame
print(df_cleaned)















