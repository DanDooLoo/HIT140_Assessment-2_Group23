import pandas as pd
import matplotlib.pyplot as plt

# read csv into a Dataframe
df = pd.read_csv("FBREF_SQUAD_STATS.csv")	

sample = df["Age"]

max_val = sample.max()
min_val = sample.min()

the_range = max_val - min_val

bin_width = 0.1

bin_count = int(the_range / bin_width)

# Creating the histogram
plt.hist(sample, color='orange', edgecolor = 'black', bins=bin_count)
plt.title('Histogram of Age')
plt.xlabel('Age')
plt.ylabel('Number of Teams')
plt.show()












