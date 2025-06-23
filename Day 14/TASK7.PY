# Random Numbers
# Create an array of 5 random numbers between 1–100.

# Create a 3x3 array with random floats between 0–1.

# Create a 4x4 array of random integers between 10–50.
import numpy as np
# Create an array of 5 random numbers between 1–100
random_numbers = np.random.randint(1, 101, size=5)
print("Array of 5 random numbers between 1–100:", random_numbers)
# Create a 3x3 array with random floats between 0–1
random_floats = np.random.rand(3, 3)
print("3x3 array with random floats between 0–1:\n", random_floats)
# Create a 4x4 array of random integers between 10–50
random_integers = np.random.randint(10, 51, size=(4, 4))
print("4x4 array of random integers between 10–50:\n", random_integers)
# Create a 2D array with random integers between 1 and 100, of shape (5, 5)
random_2d_array = np.random.randint(1, 101, size=(5, 5))
print("2D array with random integers between 1 and 100, shape (5, 5):\n", random_2d_array)