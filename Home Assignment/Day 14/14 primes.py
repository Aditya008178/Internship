# 14.	Prime Numbers with NumPy:
# o	Create an array of numbers from 1–100.
# o	Use boolean masking to filter out only the prime numbers.

import numpy as np

arr = np.arange(1, 101)

mask = np.ones_like(arr, dtype='bool')
mask[:1] = False  


for i in range(2, int(np.sqrt(len(arr))) + 1):
    if mask[i-1]:
        mask[i*i-1::i] = False


prime_numbers = arr[mask]
print(prime_numbers)
