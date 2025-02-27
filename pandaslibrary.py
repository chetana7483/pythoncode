import pandas as pd
import numpy as np

data = [10, 20, np.nan, 40, 50, 60, np.nan, 80, 90, 100]
index = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
s = pd.Series(data, index=index)


print("Original Series:\n", s)
print("\nAccess by index label 'a':", s['a'])
print("Access by position 2:", s.iloc[2])
print("\nValues greater than 50:\n", s[s > 50])
print("\nFill NaN with 0:\n", s.fillna(0))
print("Drop NaN values:\n", s.dropna())

print("\nSum:", s.sum())
print("Mean:", s.mean())
print("Median:", s.median())
print("Standard Deviation:", s.std())
print("Minimum value:", s.min())
print("Maximum value:", s.max())

print("\nIndex values:", s.index)
print("Is 'e' in index?:", 'e' in s)

print("\nSquared values using apply:\n", s.apply(lambda x: x**2))

s_str = pd.Series(['cat', 'dog', 'rabbit', 'snake'])
print("\nString Series:\n", s_str)
print("Uppercase strings:\n", s_str.str.upper())
print("Strings containing 'a':\n", s_str.str.contains('a'))

print("\nSorted by values:\n", s.sort_values())
print("Sorted by index:\n", s.sort_index())
print("Rank of values:\n", s.rank())

print("\nAggregated stats:\n", s.agg(['sum', 'min', 'max', 'mean']))

new_index = ['a', 'b', 'c', 'x', 'y', 'z']
print("\nReindexed Series:\n", s.reindex(new_index, fill_value=0))

s2 = pd.Series([1, 2, 3, 4, 5], index=['a', 'b', 'c', 'd', 'e'])
print("\nAddition with another Series:\n", s + s2)

print("\nCumulative Sum:\n", s.cumsum())

s_copy = s.copy()
print("\nCopied Series:\n", s_copy)

print("\nConvert to list:", s.tolist())
print("Convert to dictionary:", s.to_dict())
print("Convert to numpy array:", s.to_numpy())
