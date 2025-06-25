# 9.	Create a 1D array with numbers from 1–12 and:
# o	Reshape it into a 3×4 array.
# o	Flatten it back to a 1D array.

import numpy as np
array= np.array([1,2,3,4,5,6,7,8,9,10,11,12])

rs = array.reshape(3,4)
print("Reshaped array: \n", rs)

fl = array.flatten()
print("Flatten: ",fl)