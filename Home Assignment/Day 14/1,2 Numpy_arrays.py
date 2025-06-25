# Part A: Creating NumPy Arrays
# 1.	Import NumPy and:
# o	Create a 1D array with numbers from 1–10.
# o	Create a 2D array of shape (3, 3) with numbers from 1–9.
# 2.	Create an array of:
# o	All zeros (shape = (3, 3))
# o	All ones (shape = (2, 5))
# o	All random numbers (shape = (4,))

import numpy as np

array= np.array([1,2,3,4,5,6,7,8,9,10])
print("1D array of numbers from 1-10:", array)

arr2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print("\n",arr2d)

zeros = np.zeros((3, 3))
print("\n",zeros)

ones = np.ones((2, 5)) 
print("\n",ones)

r_numbers = np.random.rand(4,)
print("\n",r_numbers)



