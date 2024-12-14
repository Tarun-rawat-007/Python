import pandas as pd

df = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'City': ['New York', 'Los Angeles', 'Chicago']
}, index=['a', 'b', 'c'])
# 1. Label-based Indexing (.loc[])
# Label-based indexing allows you to access data by the labels of rows and columns. You use .loc[] with row and column labels to select specific entries, rows, or columns.

# Use case: When you know the exact labels for rows or columns.

# Accessing a single row by label
print("Row with label 'b':")
print(df.loc['b'])



# 2. Integer-based Indexing (.iloc[])
# Integer-based indexing allows you to access data by the integer positions of rows and columns. .iloc[] uses integer locations to select data.

# Use case: When you need to access rows or columns by their position.

# Accessing the second row (index position 1)
print("First row (index position 0):")
print(df.iloc[0])

# 3. Boolean Indexing
# Boolean indexing allows you to filter data based on conditions. You can create conditions and use them to select data that meets those conditions.

# Use case: Filtering rows based on one or more conditions.

# Selecting rows where Age is greater than 28
print("Rows where Age > 28:")
print([df['Age'] > 28])
print(df[df['Age'] > 28])



