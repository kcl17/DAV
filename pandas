(a)Create a series with 5 elements. Display the series sorted on index and also sorted on values seperately
import pandas as pd

# Create a series with 5 elements
series_a = pd.Series([4, 2, 8, 1, 6], index=['b', 'a', 'd', 'c', 'e'])

# Display the series
print("Original Series:")
print(series_a)

# Sort the series by index
sorted_by_index = series_a.sort_index()

# Sort the series by values
sorted_by_values = series_a.sort_values()

# Display the sorted series
print("\nSorted by Index:")
print(sorted_by_index)

print("\nSorted by Values:")
print(sorted_by_values)

(b)Create a series with N elements with some duplicate values. Find the minimum and maximum ranks
assigned to the values using ‘first’ and ‘max’ methods

import pandas as pd

# Create a series with N elements and some duplicates
series_b = pd.Series([4, 2, 8, 1, 6, 4, 8, 2])

# Find ranks using 'first' method
ranks_first = series_b.rank(method='first')

# Find ranks using 'max' method
ranks_max = series_b.rank(method='max')

# Display the original series and ranks
print("Original Series:")
print(series_b)

print("\nRanks (First Method):")
print(ranks_first)

print("\nRanks (Max Method):")
print(ranks_max)

(c)Display the index value of the minimum and maximum element of a Series

import pandas as pd

# Create a series
series_c = pd.Series([4, 2, 8, 1, 6])

# Find index of minimum and maximum element
index_min = series_c.idxmin()
index_max = series_c.idxmax()

# Display the original series and index of minimum and maximum
print("Original Series:")
print(series_c)

print("\nIndex of Minimum Element:", index_min)
print("Index of Maximum Element:", index_max)
