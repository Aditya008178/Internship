# Indexing and Slicing
# Extract the first 5 elements of an array.
# Extract the last 3 elements.
# Change every second element of an array.
# Extract an element from a 2D array.
# Slice a 2D array to get its first 2 rows and first 2 columns.

import numpy as np  

s_array = np.array([10, 20, 30, 40, 50, 60, 70, 80, 90, 100])

first_five = s_array[:5]
print("First 5 elements:", first_five)

last= s_array[-3:]
print("Last 3 elements:", last)

s_array[1::2]=5
print("Array after changing every second element:", s_array)

s2d_array = np.array([[1, 2, 3], [4, 5, 6],[7,8,9] ])

element = s2d_array[1, 2] 
print("Element at row 1, column 2:", element)


sliced_2d = s2d_array[:2, :2]

print(sliced_2d)
