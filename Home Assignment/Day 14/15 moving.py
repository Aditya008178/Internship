# 15.	Moving Averages:
# o	Given an array of daily temperatures, write a NumPy script to compute a 3 day moving average.

import numpy as np


temperatures = np.array([25, 27, 23, 24, 28, 29, 26, 27, 30])


moving_average = np.convolve(temperatures, np.ones(3)/3, mode='valid')

print(moving_average)
