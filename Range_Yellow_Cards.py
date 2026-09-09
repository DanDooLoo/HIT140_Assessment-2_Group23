import statistics as stats
import numpy as np

# range
sample = [15, 6, 8, 6, 8, 6, 7, 11, 8, 9, 7, 12, 3, 4, 7, 6, 4, 7, 8,
          3, 8, 5, 5, 5, 4, 4, 3, 7, 6, 5, 5, 5, 1, 4, 3, 6, 7, 4, 5, 2, 4, 6, 3, 4, 5, 4, 1, 4 ]

the_range = np.max(sample) - np.min(sample)
print("Range: %d" % the_range)
