# for finding which high possession match didn't have a low possession counterpart in samples
# for easier data extraction

import pandas as pd

high = pd.read_csv("high_possession_sample.csv")
low = pd.read_csv("low_possession_sample.csv")

missing = high[~high["Match ID"].isin(low["Match ID"])]
print(missing)
