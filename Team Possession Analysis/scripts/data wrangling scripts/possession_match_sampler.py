import pandas as pd

df = pd.read_csv("match_list_with_ids.csv")

high = df[(df["Home Possession"] >= 0.65) | (df["Away Possession"] >= 0.65)]
high.to_csv("high_possession_list.csv", index=False)

low = df[(df["Home Possession"] <= 0.35) | (df["Away Possession"] <= 0.35)]
low.to_csv("low_possession_list.csv", index=False)
