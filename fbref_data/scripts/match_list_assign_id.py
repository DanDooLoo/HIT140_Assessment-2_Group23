# for assigning each match an ID

import pandas as pd

df = pd.read_csv("fbref_match_possession_shots_cleaned_names.csv")

df["Match ID"] = range(1, len(df) + 1)

df.to_csv("match_list_with_ids.csv", index=False)
