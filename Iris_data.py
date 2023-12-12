import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn import datasets
from scipy import stats

# a. Load data into a pandas data frame
iris = datasets.load_iris()
iris_df = pd.DataFrame(data=iris.data, columns=iris.feature_names)
iris_df['target'] = iris.target

# Display information on data types in the dataset
print("Info on Data Types in the Dataset:")
print(iris_df.info())

# b. Find the number of missing values in each column
missing_values = iris_df.isnull().sum()
print("\nb. Number of Missing Values in Each Column:")
print(missing_values)

# c. Plot bar chart to show the frequency of each class label
plt.figure(figsize=(6, 4))
sns.countplot(x='target', data=iris_df)
plt.title('Frequency of Each Class Label')
plt.xlabel('Class Label')
plt.ylabel('Count')
plt.show()

# d. Draw a scatter plot for Petal Length vs Sepal Length and fit a regression line
plt.figure(figsize=(8, 6))
sns.regplot(x='sepal length (cm)', y='petal length (cm)', data=iris_df)
plt.title('Scatter Plot: Petal Length vs Sepal Length')
plt.xlabel('Sepal Length (cm)')
plt.ylabel('Petal Length (cm)')
plt.show()

# e. Plot density distribution for feature Petal width
plt.figure(figsize=(8, 6))
sns.kdeplot(iris_df['petal width (cm)'], shade=True)
plt.title('Density Distribution for Petal Width')
plt.xlabel('Petal Width (cm)')
plt.ylabel('Density')
plt.show()

# f. Use a pair plot to show pairwise bivariate distribution in the Iris Dataset
plt.figure(figsize=(10, 8))
sns.pairplot(iris_df, hue='target', markers=["o", "s", "D"])
plt.title('Pairwise Bivariate Distribution in the Iris Dataset')
plt.show()

# g. Draw heatmap for any two numeric attributes
plt.figure(figsize=(8, 6))
sns.heatmap(iris_df[['sepal length (cm)', 'petal length (cm)']].corr(), annot=True, cmap='coolwarm')
plt.title('Heatmap for Sepal Length and Petal Length')
plt.show()

# h. Compute mean, mode, median, standard deviation, confidence interval, and standard error for each numeric feature
numeric_features = iris_df.columns[:-1]
statistics_df = iris_df[numeric_features].describe().transpose()
statistics_df['mode'] = iris_df[numeric_features].mode().transpose().iloc[:, 0]
confidence_interval = iris_df[numeric_features].apply(lambda x: stats.t.interval(0.95, len(x)-1, loc=x.mean(), scale=stats.sem(x)))
statistics_df['confidence_interval'] = [f"{round(interval[0], 2)} - {round(interval[1], 2)}" for interval in confidence_interval.values]
statistics_df['standard_error'] = iris_df[numeric_features].apply(stats.sem)
print("\nh. Statistics for Each Numeric Feature:")
print(statistics_df)

# i. Compute correlation coefficients between each pair of features and plot heatmap
correlation_matrix = iris_df[numeric_features].corr()
plt.figure(figsize=(8, 6))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm')
plt.title('Correlation Coefficients Heatmap')
plt.show()
