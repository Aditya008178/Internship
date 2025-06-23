# Reshaping and Flattening
# Create an array with numbers from 1–12 and reshape it into (3, 4).
# Flatten the array back into a 1D array.

import numpy as np


r=np.array([1,2,3,4,5,6,7,8,9,10,11,12])
print(f"Original Array:{r}")


rs=r.reshape(3,4)
print("Reshaped array (3, 4):\n", rs)


f=rs.flatten()
print("Flattened array:", f)
