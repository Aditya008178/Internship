# 12.	Create a 5x5 array of random numbers between 10–100 and:
# o	Find its transpose
# o	Find the sum of its diagonal
# o	Extract the diagonal elements

import numpy as np
arr = np.random.randint(10, 100, (5, 5))
print("Array: \n",arr)

print("\nTranspose: \n",arr.T)

print("\nSum of its diagonal",np.trace(arr))

print("\n Extract the diagonal elements: ", np.diag(arr))