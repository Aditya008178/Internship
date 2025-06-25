# 5.	Create an array:
# arr = np.arange(1, 21).reshape(4, 5)
# o	Print the first row.
#  o	Print the last column.
#  o	Slice the subarray of the first 2 rows and first 3 columns.
import numpy as np
arr = np.arange(1, 21).reshape(4, 5)

print("First row")
print(arr[1])

print("Last column")
print(arr[:,-1])

print("first 2 rows and first 3 columns")
print(arr[:2,:3])