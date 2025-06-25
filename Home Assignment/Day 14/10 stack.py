# 10.	Stack arrays:
# o	Create a = [1, 2, 3] and b = [4, 5, 6]
# o	Stack them vertically and horizontally.

import numpy as np

a1 = np.array([1, 2, 3])
a2 = np.array([4, 5, 6])

vs = np.vstack((a1,a2))
print("Vertically Satck: \n",vs)

hs = np.hstack((a1,a2))
print("\nHorizontally Stack: \n",hs)