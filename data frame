import pandas as pd
import numpy as np

# Create a DataFrame with 3 columns and 50 rows
np.random.seed(42)  # Setting seed for reproducibility
data = {
    'Column1': np.random.rand(50),
    'Column2': np.random.rand(50),
    'Column3': np.random.rand(50)
}
df = pd.DataFrame(data)

# Replace 10% of values with null values
null_indices = np.random.choice(df.size, int(0.1 * df.size), replace=False)
df.values.flat[null_indices] = np.nan

# Display the original DataFrame
print("Original DataFrame:")
print(df)

# a. Identify and count missing values in the DataFrame
missing_values = df.isnull()
missing_count = missing_values.sum().sum()
print("\na. Missing Values Count:", missing_count)

# b. Drop the column having more than 5 null values
df = df.dropna(axis=1, thresh=len(df) - 5)
print("\nb. DataFrame after dropping columns with more than 5 null values:")
print(df)

# c. Identify the row label having the maximum sum of all values in a row and drop that row
max_sum_row_label = df.sum(axis=1).idxmax()
df = df.drop(max_sum_row_label)
print("\nc. DataFrame after dropping the row with the maximum sum:")
print(df)

# d. Sort the DataFrame based on the first column
df = df.sort_values(by='Column1')
print("\nd. DataFrame sorted based on the first column:")
print(df)

# e. Remove all duplicates from the first column
df = df.drop_duplicates(subset='Column1')
print("\ne. DataFrame after removing duplicates from the first column:")
print(df)

# f. Find the correlation between the first and second column, and covariance between the second and third column
correlation = df['Column1'].corr(df['Column2'])
covariance = df['Column2'].cov(df['Column3'])
print("\nf. Correlation between Column1 and Column2:", correlation)
print("   Covariance between Column2 and Column3:", covariance)

# g. Discretize the second column and create 5 bins
df['Column2_bins'] = pd.cut(df['Column2'], bins=5)
print("\ng. DataFrame after discretizing the second column into 5 bins:")
print(df)
