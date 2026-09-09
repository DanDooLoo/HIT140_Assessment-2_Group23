import statistics as stats
import numpy as np

#mean
sample = [15, 6, 8, 6, 8, 6, 7, 11, 8, 9, 7, 12, 3, 4, 7, 6, 4, 7, 8, 3, 8, 5, 5, 5, 4, 4, 3, 7, 6, 5, 5, 5, 1, 4, 3, 6, 7, 4, 5, 2, 4, 6, 3, 4, 5, 4, 1, 4]
x_bar = stats.mean(sample)
print("Mean:", x_bar)

# median
sample = [15, 6, 8, 6, 8, 6, 7, 11, 8, 9, 7, 12, 3, 4, 7, 6, 4, 7, 8, 3, 8, 5, 5, 5, 4, 4, 3, 7, 6, 5, 5, 5, 1, 4, 3, 6, 7, 4, 5, 2, 4, 6, 3, 4, 5, 4, 1, 4]
median = stats.median(sample)
print("Median: %.2f" % median)

# range
sample = [15, 6, 8, 6, 8, 6, 7, 11, 8, 9, 7, 12, 3, 4, 7, 6, 4, 7, 8, 3, 8, 5, 5, 5, 4, 4, 3, 7, 6, 5, 5, 5, 1, 4, 3, 6, 7, 4, 5, 2, 4, 6, 3, 4, 5, 4, 1, 4 ]
the_range = np.max(sample) - np.min(sample)
print("Range: %d" % the_range)

#sample and population variance
sample = np.array([15, 6, 8, 6, 8, 6, 7, 11, 8, 9, 7, 12, 3, 4, 7, 6, 4, 7, 8, 3, 8, 5, 5, 5, 4, 4, 3, 7, 6, 5, 5, 5, 1, 4, 3, 6, 7, 4, 5, 2, 4, 6, 3, 4, 5, 4, 1, 4])
s_square = sample.var(ddof=1)
sigma_square = sample.var()
print("Sample variance: %.2f. Population variance: %.2f" % (s_square, sigma_square))

#sample and population standard deviation
s = sample.std(ddof=1)
sigma = sample.std()
print("Sample std. dev.: %.2f. Population std. dev.: %.2f." % (s, sigma))
