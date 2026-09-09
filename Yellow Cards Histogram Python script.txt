import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("FIFA_Discipline_YC.csv")

sample = df["Yellow_Cards"]

max_val = sample.max()
min_val = sample.min()

the_range = max_val - min_val

bin_width = 1

bin_count = int(the_range / bin_width)

# 6. Create the histogram 

plt.hist(sample, color='orange', edgecolor='black', bins=bin_count)

plt.title('Histogram of Yellow Cards')

# Swapped these labels so they make visual sense for a histogram

plt.xlabel('Number of Yellow Cards')

plt.ylabel('Number of Teams')

# 7. Show the final graph

plt.show()