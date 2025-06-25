# 13.	Compare Lists vs NumPy:
# o	Create a Python list and a NumPy array of the same data.
# o	Compare their memory usage using sys.getsizeof() and .nbytes.
# o	Compare their performance for an operation like adding 1 to every element.


import sys
import numpy as np
import time


data = list(range(1000000))
arr = np.array(data)


l_memory = sys.getsizeof(data)
a_memory = arr.nbytes
print(f"Memory usage - List: {l_memory} bytes, NumPy array: {a_memory} bytes")

# Compare their performance for an operation like adding 1 to every element
start_time = time.time()
new_list = [x + 1 for x in data]
list_time = time.time() - start_time

start_time = time.time()
new_arr = arr + 1
array_time = time.time() - start_time

print(f"Time taken - List: {list_time:.6f} seconds, NumPy array: {array_time:.6f} seconds")
