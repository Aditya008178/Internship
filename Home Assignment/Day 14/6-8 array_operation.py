# 6.	Elementwise operations:
# o	Create two arrays of the same shape (e.g., a = [[1,2],[3,4]], b = [[5,6],[7,8]])
# o	Perform elementwise:
# 	Addition
# 	Subtraction
# 	Multiplication
# 	Division
# 7.	Find:
# o	Sum of all elements
# o	Min, max, and average of an array
# 8.	Use NumPy to compute:
# o	Square root of every element in an array
# o	Square of every element in an array

import numpy as np
arr1 = np.array([[1,2],[3,4]])
arr2 = np.array([[5,6],[7,8]])

add = arr1 + arr2
sub = arr1 - arr2
mul = arr1 * arr2
Div = arr1 / arr2

print("Element wise Addition: ",add)
print("Element wise Subtraction: ",sub)
print("Element wise Multiplication: ",mul)
print("Element wise Division: ",Div)


s_array = np.array([11, 5, 67, 34, 98])

m = np.min(s_array)
print("\nMinimum: ",m)

Max = np.max(s_array)
print("Maximum: ",Max)

avg = np.average(s_array)
print("Average: ",avg)

s_root = np.sqrt(s_array)
print("Square root: ",s_root)

sqr = np.square(s_array)
print("Square: ",sqr)