import pandas as pd

df = pd.read_csv("match_list_with_ids.csv")

df["Match ID"] = df["Match ID"].astype(int).astype(str).str.zfill(3)

df.to_csv("match_list_with_ids.csv", index=False)
