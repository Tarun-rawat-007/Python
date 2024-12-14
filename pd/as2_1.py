import pandas as pd

print("Creating a Series:") 
series = pd.Series([10, 20, 30, 40], index=['a', 'b', 'c', 'd'])
print(series)

print("Accessing data by label:",series['b'])  


print("Modifying data:")
series['b'] = 50
print(series)


print("Creating a DataFrame:")
df = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'City': ['New York', 'Los Angeles', 'Chicago']
}, index=['a', 'b', 'c'])
print(df)


print("\nAccessing the 'Age' column:")
print(df['Age'])


print("\nAccess a Row by Position (iloc):")
print(df.iloc[0])


print("\nAccess a Row by Label (loc):")
print(df.loc['a'])

# Correct way to modify a column value by label
df.at['b', 'Age'] = 32

# Adding a new column
df['Country'] = ['USA', 'USA', 'USA']
print("\nDataFrame after modification and adding a new column:")
print(df)
