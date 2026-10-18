import pandas as pd
import os

os.chdir(os.path.dirname(__file__))

df = pd.read_csv("match_list_no_penalties.csv")

# splitting the score column
df["Score"] = df["Score"].str.replace("–", "-", regex=False)

scores = df["Score"].str.split("-", expand=True)

df["Home Goals"] = scores[0].astype(int)
df["Away Goals"] = scores[1].astype(int)

# create home rows
home_df = pd.DataFrame({
    "Match ID": df["Match ID"],
    "Date": df["Date"],
    "Team": df["Home"],
    "H/A": "Home",
    "Goals": df["Home Goals"],
    "Referee": df["Referee"]
})

away_df = pd.DataFrame({
    "Match ID": df["Match ID"],
    "Date": df["Date"],
    "Team": df["Away"],
    "H/A": "Away",
    "Goals": df["Away Goals"],
    "Referee": df["Referee"]
})

team_df = pd.concat(
    [home_df, away_df],
    ignore_index=True
)

team_df.to_csv("team_level_dataset.csv", index=False)
