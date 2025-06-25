# Create a 1D array of numbers from 1–10.

# Create an array of 10 zeros.  

# Create an array of 5 ones.

# Create an array of even numbers from 2–20.

# Create an array with random numbers between 0 and 1.

# Create an array of shape (3, 3) filled with the number 7.

# Create an identity matrix of size 4x4
import numpy as np
array= np.array([1,2,3,4,5,6,7,8,9,10])
print("1D array of numbers from 1–10:", array)
zeros_array = np.zeros(10)
print("Array of 10 zeros:", zeros_array)
ones_array = np.ones(5)
print("Array of 5 ones:", ones_array)
even_numbers = np.arange(2, 21, 2)
print("Array of even numbers", even_numbers)

random_numbers = np.random.rand(10)
print("Array with random numbers:", random_numbers)
seven_array = np.full((3, 3), 7)
print("Array of shape (3, 3)\n", seven_array)
identity_matrix = np.eye(4)
print("Identity matrix of size 4x4:\n", identity_matrix)
