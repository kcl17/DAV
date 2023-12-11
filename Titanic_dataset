import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load Titanic dataset
titanic = sns.load_dataset('titanic')

# Display the information about missing values
print("Info on Missing Values in the Titanic Dataset:")
print(titanic.isnull().sum())

# a. Clean the data by dropping the column which has the largest number of missing values
column_with_most_missing = titanic.isnull().sum().idxmax()
titanic_cleaned = titanic.drop(column_with_most_missing, axis=1)
print("\na. Titanic Data After Dropping Column with Most Missing Values:")
print(titanic_cleaned.head())

# b. Find total number of passengers with age more than 30
passengers_over_30 = titanic_cleaned[titanic_cleaned['age'] > 30]
total_passengers_over_30 = len(passengers_over_30)
print("\nb. Total Number of Passengers with Age More Than 30:", total_passengers_over_30)

# c. Find total fare paid by passengers of second class
total_fare_second_class = titanic_cleaned[titanic_cleaned['pclass'] == 2]['fare'].sum()
print("\nc. Total Fare Paid by Passengers of Second Class:", total_fare_second_class)

# d. Compare number of survivors of each passenger class
survivors_by_class = titanic_cleaned.groupby('pclass')['survived'].sum()
print("\nd. Number of Survivors by Passenger Class:")
print(survivors_by_class)

# e. Compute descriptive statistics for age attribute gender wise
descriptive_stats_age_gender = titanic_cleaned.groupby('sex')['age'].describe()
print("\ne. Descriptive Statistics for Age Attribute Gender Wise:")
print(descriptive_stats_age_gender)

# f. Draw a scatter plot for passenger fare paid by Female and Male passengers separately
plt.figure(figsize=(8, 6))
sns.scatterplot(x='fare', y='sex', data=titanic_cleaned)
plt.title('Scatter Plot: Passenger Fare Paid by Female and Male Passengers')
plt.xlabel('Fare')
plt.ylabel('Gender')
plt.show()

# g. Compare density distribution for features age and passenger fare
plt.figure(figsize=(12, 6))
plt.subplot(1, 2, 1)
sns.kdeplot(titanic_cleaned['age'], shade=True)
plt.title('Density Distribution for Age')
plt.xlabel('Age')
plt.ylabel('Density')

plt.subplot(1, 2, 2)
sns.kdeplot(titanic_cleaned['fare'], shade=True)
plt.title('Density Distribution for Passenger Fare')
plt.xlabel('Fare')
plt.ylabel('Density')

plt.tight_layout()
plt.show()

# h. Draw the pie chart for three groups labelled as class 1, class 2, class 3
passenger_class_counts = titanic_cleaned['pclass'].value_counts()
plt.figure(figsize=(8, 8))
plt.pie(passenger_class_counts, labels=['Class 1', 'Class 2', 'Class 3'], autopct='%1.1f%%', colors=['skyblue', 'lightgreen', 'lightcoral'])
plt.title('Pie Chart: Distribution of Passenger Classes')
plt.show()

# i. Find % of survived passengers for each class
survival_percentage_by_class = titanic_cleaned.groupby('pclass')['survived'].mean() * 100
print("\ni. Percentage of Survived Passengers for Each Class:")
print(survival_percentage_by_class)

# Did class play a role in survival?
# From the percentages calculated in part (i), we can observe the survival rates for each class.
# This information can be used to answer the question.
