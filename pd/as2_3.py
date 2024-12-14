import pandas as pd

s1 = pd.Series([2, 2, 3], index=['a', 'b', 'c'])
s2 = pd.Series([4, 5, 6], index=['a', 'd', 'c'])


print("Aligned automatically aligned by index Series Addition:")
result = s1 + s2
print(result)

df = pd.DataFrame({
    'A': [1, None, 3],
    'B': [4, 5, 6],
    'C': [None, 4, 9]
})

print("\nOriginal DataFrame:")
print(df)

print("\nDataFrame after dropping rows with NaN:")
print(df.dropna())


print("\nDataFrame after dropping columns with NaN:")
print(df.dropna(axis=1))


print("\nDataFrame after filling NaN with 0:")
print(df.fillna(0))


print("\nDataFrame after filling NaN with column mean:")
print(df.fillna(df.mean()))


print("\nDataFrame after forward fill (ffill):")
print(df.ffill())


print("\nDataFrame after backward fill (bfill):")
print(df.bfill())
