# 12.	Import the statistics module:
# o	Calculate the mean and median of the list [1, 2, 3, 4, 5, 100].

import statistics
list = [1, 2, 3, 4, 5, 100]
mean = statistics.mean(list)
median = statistics.median(list)

print("Mean: ", mean)
print("Median: ", median)