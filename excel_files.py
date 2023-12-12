import pandas as pd

# Assuming you have two Excel files named 'workshop1.xlsx' and 'workshop2.xlsx'
# Each file has three columns: 'Name', 'Date', 'Duration'

# a. Import data into two data frames
df1 = pd.read_excel('workshop1.xlsx')
df2 = pd.read_excel('workshop2.xlsx')

# Display the original data frames
print("Data Frame 1:")
print(df1)

print("\nData Frame 2:")
print(df2)

# b. Perform merging to find names of students who attended both workshops
both_workshops = pd.merge(df1, df2, how='inner', on=['Name', 'Date'])
print("\nNames of Students who Attended Both Workshops:")
print(both_workshops['Name'].unique())

# c. Find names of students who attended a single workshop only
single_workshop = pd.concat([df1, df2]).drop_duplicates(keep=False)
print("\nNames of Students who Attended a Single Workshop Only:")
print(single_workshop['Name'].unique())

# d. Merge two data frames row-wise and find the total number of records
merged_row_wise = pd.concat([df1, df2], ignore_index=True)
print("\nMerged Data Frame Row-Wise:")
print(merged_row_wise)

# e. Generate descriptive statistics for the hierarchical data frame
hierarchical_df = pd.concat([df1.set_index(['Name', 'Date']), df2.set_index(['Name', 'Date'])])
descriptive_stats = hierarchical_df.groupby(['Name', 'Date']).describe()
print("\nDescriptive Statistics for Hierarchical Data Frame:")
print(descriptive_stats)
