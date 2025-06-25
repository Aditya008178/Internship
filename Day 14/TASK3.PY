# Inspecting Arrays

# Create a sample array of float64

# Find the shape, size, and dtype of an array.

# Change the dtype of an array from float64 to int32.

# Find the number of dimensions (ndim) of an array.
import numpy as np
# Create a sample array of float64
sample_array = np.array([1.5, 2.5, 3.5], dtype=np.float64)
#2d array
sample_array_2d = np.array([[1.5, 2.5], [3.5, 4.5]], dtype=np.float64)
print("Sample array:", sample_array)
# Find the shape, size, and dtype of an array
print("Shape of the array:", sample_array.shape)
print("Size of the array:", sample_array.size)
# Change the dtype from float64 to int32 using .astype()

sample_array_int32 = sample_array.astype(np.int32)
print(sample_array_int32.dtype)