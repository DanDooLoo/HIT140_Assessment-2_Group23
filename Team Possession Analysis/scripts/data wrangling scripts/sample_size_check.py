# for checking if certain possession values have viable sample sizes

import pandas as pd

df = pd.read_csv("fbref_match_possession_shots_cleaned_names.csv")

high_home = df[df["Home Possession"] >= 0.65]
high_away = df[df["Away Possession"] >= 0.65]

low_home = df[df["Home Possession"] <= 0.35]
low_away = df[df["Away Possession"] <= 0.35]

print("High home possession:", len(high_home))
print("High away possession:", len(high_away))
print("Low home possession:", len(low_home))
print("Low away possession:", len(low_away))
print("Total high possession teams:", len(high_home) + len(high_away))
print("Total low possession teams:", len(low_home) + len(low_away))
print(df.columns)
