import pandas as pd

data = {
    'Store': ['A', 'B', 'C', 'D', 'E'],
    'Region': ['North', 'South', 'East', 'West', 'North'],
    'Sales': [2500, 3000, 1500, 2800, 2200],
    'Employees': [10, 15, 8, 12, 11]
}

df = pd.DataFrame(data)
df.set_index('Store', inplace=True)
df['Sales_Per_Employee'] = df['Sales'] / df['Employees']
filtered_stores = df[df['Sales'] > 2000]
sorted_stores = filtered_stores.sort_values(by='Sales', ascending=False)
df['Sales'] = df['Sales'].fillna(df['Sales'].mean())

print("DataFrame with 'Store' as index and new column 'Sales_Per_Employee':")
print(df)
print("\nFiltered stores with Sales > 2000:")
print(filtered_stores)
print("\nSorted stores by Sales in descending order:")
print(sorted_stores)
