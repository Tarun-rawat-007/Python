import pandas as pd

data = {
    'Store': ['A', 'B', 'C', 'D', 'E'],
    'Region': ['North', 'South', 'East', 'West', 'North'],
    'Sales': [2500, 3000, 1500, 2800, 2200],
    'Employees': [10, 15, 8, 12, 11]
}

df = pd.DataFrame(data)

# Set 'Store' as the index
df.set_index('Store', inplace=True)
print("After setting 'Store' as index:")
print(df)

# Add 'Sales_Per_Employee' column
df['Sales_Per_Employee'] = df['Sales'] / df['Employees']
print("\nAfter adding 'Sales_Per_Employee' column:")
print(df)

# Filter stores with Sales > 2000
filtered_stores = df[df['Sales'] > 2000]
print("\nFiltered stores with Sales > 2000:")
print(filtered_stores)

# Sort by 'Sales' in descending order
sorted_stores = filtered_stores.sort_values(by='Sales', ascending=False)
print("\nSorted stores by Sales in descending order:")
print(sorted_stores)

# Fill missing values in 'Sales' with the mean
df['Sales'] = df['Sales'].fillna(df['Sales'].mean())
print("\nAfter filling missing 'Sales' values with the mean:")
print(df)
