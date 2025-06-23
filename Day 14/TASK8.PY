# Final Mini Project
# Perform the following in one script:
# Create a 5x5 array of random integers between 1–100.
# Find the min, max, mean, and sum of the array.
# Replace all numbers > 50 with -1.
# Save the array to a .npy file.
# Load it back and print the contents.

import numpy as np
# Create a 5x5 array of random integers between 1–100
random_array = np.random.randint(1, 101, size=(5, 5))
print("5x5 Array of Random Integers between 1–100:\n", random_array)
# Find the min, max, mean, and sum of the array
min_value = np.min(random_array)
max_value = np.max(random_array)
mean_value = np.mean(random_array)
sum_value = np.sum(random_array)
print("Minimum Value:", min_value)
print("Maximum Value:", max_value)
print("Mean Value:", mean_value)
print("Sum of Values:", sum_value)
# Replace all numbers > 50 with -1
random_array[random_array > 50] = -1
print("Array after replacing numbers > 50 with -1:\n", random_array)
# Save the array to a .npy file
np.save('random_array.npy', random_array)
# Load it back and print the contents
loaded_array = np.load('random_array.npy')
