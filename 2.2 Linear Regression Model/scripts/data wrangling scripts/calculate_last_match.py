import pandas as pd
import os

os.chdir(os.path.dirname(__file__))

master = pd.read_csv("208_dataset_MFP.csv")

master["Date"] = pd.to_datetime(master["Date"])
master = master.sort_values(["Team", "Date"])

master["DLG"] = (
    master.groupby("Team")["Date"]
    .diff()
    .dt.days
)

print(master[["Match ID", "Team", "DLG"]].head())

master = master.sort_values(["Match ID", "H/A"])

print(master[["Match ID", "Team", "DLG"]].head())

master["DLG"] = (
    master["DLG"].fillna(0)
)

master.to_csv("test.csv", index=False)