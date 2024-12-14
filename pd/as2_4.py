import pandas as pd


df1 = pd.DataFrame({
    'Name': ['Alice', 'Bob'],
    'DepartmentID': [101, 102]
})

df2 = pd.DataFrame({
    'Name': ['David' ],
    'DepartmentID': [102]
})


print("DataFrame df1:\n",df1)
print("DataFrame df2:\n",df2)

print("\nConcatenated DataFrame (df1 and df2):")
result_concat = pd.concat([df1, df2], ignore_index=True)
print(result_concat)


print("\nInner Join :",pd.merge(df1, df2, on='DepartmentID', how='inner'))


print("\nOuter Join :",pd.merge(df1, df2, on='DepartmentID', how='outer'))



print("\nLeft Join :")
result_left = pd.merge(df1, df2, on='DepartmentID', how='left')
print(result_left)

print("\nRight Join :")
result_right = pd.merge(df1, df2, on='DepartmentID', how='right')
print(result_right)


# In the context of the provided code,  Here's a breakdown of the inner and outer join operations performed in the code:

# 1. Joining on Index
# When you use the join method, you are aligning the two DataFrames based on their indices rather than on a specific column. This means that the rows are combined based on their index labels.
# Joining on index
print("\nJoin (inner join on index):")
result_join_inner = df1.join(df2, how='inner', lsuffix='_emp', rsuffix='_wrk')
print(result_join_inner)

print("\nJoin (outer join on index):")
result_join_outer = df1.join(df2, how='outer', lsuffix='_emp', rsuffix='_wrk')
print(result_join_outer)