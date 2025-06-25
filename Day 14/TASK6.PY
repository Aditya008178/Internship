# Math Operations
# Perform element-wise addition, subtraction, multiplication, and division between two arrays.
# Perform power and square root operations.
# Use np.sum(), np.mean(), np.min(), np.max(), and np.std().

import numpy as np

array1 = np.array([1, 2, 3, 4, 5])
array2 = np.array([6, 7, 8, 9, 10])
addition = array1 + array2
subtraction = array1 - array2
multiplication = array1 * array2
division = array1 / array2
print("Element-wise Addition:", addition)
print("Element-wise Subtraction:", subtraction)
print("Element-wise Multiplication:", multiplication)
print("Element-wise Division:", division)


power = array1 ** 2
square_root = np.sqrt(array1)
print("Power:", power)
print("Square Root of array1:", square_root)

sum=np.sum(array1)
print("Sum of array1:", sum)

mean=np.mean(array1)
print("Mean of array1:", mean)

min_value = np.min(array1)
print("Minimum value in array1:", min_value)

max_value = np.max(array1)
print("Maximum value in array1:", max_value)

std_dev = np.std(array1)
print("Standard Deviation of array1:", std_dev)


array2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])