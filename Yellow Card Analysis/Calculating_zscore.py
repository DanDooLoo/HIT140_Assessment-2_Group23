import scipy.stats as st
import math

# Process of calculating the sample mean, standard deviation, and sample size
median = 5.625
s = 48
n = 270
print("Mean: %.2f. Standard deviation: %2f. Size: %d." % (median, s, n))

#z-score (assuming 95% Confidence Level)
z_score = st.norm.ppf(q=0.975)
print("z-statistic: %2f" % z_score)

#compute standard error
std_err = s / math.sqrt(n)
print("Standard error: %.2f" % std_err)

# compute the margin of error
mrg_err = z_score * std_err
print("Margin of error: %2f" % mrg_err)

#get the lower and upper bound of confidence level
ci_low = median - mrg_err
ci_upp = median + mrg_err

print("Confidence Interval of the mean: %.2f to %.2f" % (ci_low, ci_upp))
