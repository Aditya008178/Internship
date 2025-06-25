# 🔹 Part B: Inspecting Arrays
# 3.	Given:
# arr = np.arange(12).reshape(3, 4)
# o	Print its shape, size, ndim, and dtype.
# 4.	Change the dtype of an array from float64 to int32.

import numpy as np

arr = np.arange(12).reshape(3 ,4)

print("Shape: ", arr.shape)
print("Size: ", arr.size)
print("Dimension: ", arr.ndim)
print("Datatype: ", arr.dtype)

print("\nChanging data type of array")

arr2 = np.array([1.5, 2.5, 3.5], dtype=np.float64)
arr2_int32 = arr2.astype(np.int32)
print(arr2_int32.dtype)