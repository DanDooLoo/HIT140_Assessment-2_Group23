import pandas as pd
import os

os.chdir(os.path.dirname(__file__))

master = pd.read_csv("208_dataset_WC22GS.csv")

rp = master.sort_values(["Team", "Date"])

rp["RP"] = (
    rp.groupby("Team")["Goals"]
    .transform(lambda x: x.shift(1).rolling(3, min_periods=1).mean())
)

rp = rp[["Match ID", "H/A", "RP"]].copy()

print(rp.head())
print(master.head())

master = master.merge(
    rp,
    on=["Match ID", "H/A"],
    how="left"
)

master.to_csv("208_dataset_RP.csv", index=False)