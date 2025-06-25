# 11.	Create an array of 100 random numbers and:
# o	Find the top 5 maximum numbers
# o	Find the average
# o	Find the indices of all numbers > 50

import numpy as np
arr = np.random.randint(0,100,100)

maximum5 = np.sort(arr)[-5:]
print("Top 5 maximum numbers: ",maximum5)

average = np.mean(arr)
print("Average: ",average)

indices = np.where(arr>50)[0]
print("Indices of all numbers > 50: ",indices)
