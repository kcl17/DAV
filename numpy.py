
* q1 a) *
  
#Create a two dimensional array, ARR1 having random values from 0 to 1. Compute the mean, standard
#deviation, and variance of ARR1 along the second axis.

import numpy as np

# Create a 2D array with random values
ARR1 = np.random.rand(3, 5)

# Compute mean, standard deviation, and variance along the second axis
mean_values = np.mean(ARR1, axis=1)
std_dev_values = np.std(ARR1, axis=1)
variance_values = np.var(ARR1, axis=1)

print("ARR1:\n", ARR1)
print("Mean along axis 1:", mean_values)
print("Standard Deviation along axis 1:", std_dev_values)
print("Variance along axis 1:", variance_values)

* B *

#Create a 2-dimensional array of size m x n integer elements, also print the shape, type and data type of
#the array and then reshape it into an n x m array, where n and m are user inputs given at the run time.

import numpy as np

# Take user inputs for dimensions
m = int(input("Enter number of rows (m): "))
n = int(input("Enter number of columns (n): "))

# Create a 2D array of size m x n
arr = np.random.randint(0, 10, size=(m, n))

# Display shape, type, and data type of the array
print("Original Array:")
print("Shape:", arr.shape)
print("Type:", type(arr))
print("Data Type:", arr.dtype)

# Reshape the array to n x m
arr_reshaped = arr.reshape((n, m))

# Display the reshaped array
print("\nReshaped Array:")
print(arr_reshaped)

* C *
#Test whether the elements of a given 1D array are zero, non-zero and NaN. Record the indices of these
#elements in three separate arrays.

import numpy as np

# Create a 1D array
arr = np.array([1, 0, 3, 0, np.nan, 5])

# Test for zero, non-zero, and NaN
zero_indices = np.where(arr == 0)[0]
non_zero_indices = np.where(arr != 0)[0]
nan_indices = np.where(np.isnan(arr))[0]

print("Array:", arr)
print("Zero Indices:", zero_indices)
print("Non-zero Indices:", non_zero_indices)
print("NaN Indices:", nan_indices)

* D * 

#Create three random arrays of the same size: Array1, Array2 and Array3. Subtract Array 2 from Array3
#and store in Array4. Create another array Array5 having two times the values in Array1. Find Co-
#variance and Correlation of Array1 with Array4 and Array5 respectively.
import numpy as np

# Create random arrays
Array1 = np.random.rand(5)
Array2 = np.random.rand(5)
Array3 = np.random.rand(5)

# Subtract Array2 from Array3 and store in Array4
Array4 = Array3 - Array2

# Create Array5 with two times the values in Array1
Array5 = 2 * Array1

# Find Covariance and Correlation
covariance = np.cov(Array1, Array4)[0, 1]
correlation = np.corrcoef(Array1, Array5)[0, 1]

print("Array1:", Array1)
print("Array2:", Array2)
print("Array3:", Array3)
print("Array4 (Array3 - Array2):", Array4)
print("Array5 (2 * Array1):", Array5)
print("Covariance of Array1 and Array4:", covariance)
print("Correlation of Array1 and Array5:", correlation)

* E *
#Create two random arrays of the same size 10: Array1, and Array2. Find the sum of the first half of both
#the arrays and product of the second half of both the arrays.


import numpy as np

# Create two random arrays
Array1 = np.random.rand(10)
Array2 = np.random.rand(10)

# Sum of the first half of both arrays
sum_first_half = np.sum(Array1[:5]) + np.sum(Array2[:5])

# Product of the second half of both arrays
product_second_half = np.prod(Array1[5:]) * np.prod(Array2[5:])

print("Array1:", Array1)
print("Array2:", Array2)
print("Sum of the first half of both arrays:", sum_first_half)
print("Product of the second half of both arrays:", product_second_half)

* F *
#Create an array with random values. Determine the size of the memory occupied by the array.

import numpy as np

# Create an array with random values
arr = np.random.rand(3, 4)

# Determine the size of memory occupied by the array
memory_size = arr.nbytes

print("Array:")
print(arr)
print("Size of Memory Occupied:", memory_size, "bytes")

* G *
#Create a 2-dimensional array of size m x n having integer elements in the range (10,100). Write
#statements to swap any two rows, reverse a specified column and store updated array in another
#variable

import numpy as np

# Create a 2D array of size m x n
m, n = 3, 4
array_2d = np.random.randint(10, 100, size=(m, n))

print("Original Array:")
print(array_2d)

# Swap Rows
array_2d[[0, 2]] = array_2d[[2, 0]]

# Reverse a Specified Column (e.g., reverse the second column)
array_2d[:, 1] = array_2d[::-1, 1]

print("\nUpdated Array:")
print(array_2d)
