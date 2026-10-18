import pandas as pd
import os

os.chdir(os.path.dirname(__file__))

players = pd.read_csv("WC26_allplayers_exp.csv")
master = pd.read_csv("208_dataset_WC22XP.csv")

age_parts = players["Age"].str.split("-", expand=True)

players["Age Decimal"] = (
    age_parts[0].astype(float)
    + age_parts[1].astype(float) / 365.25
)

players["Team Type"] = players["Team Type"].replace({
    "home": "Home",
    "away": "Away"
})

# players.to_csv("WC26_allplayers_age.csv", index="False")

team_age = (
    players
    .groupby(["Match ID", "Team Type"], as_index=False)["Age Decimal"]
    .mean()
)

team_age = team_age.rename(
    columns={"Age Decimal": "Average Team Age"}
)

team_age.to_csv("WC26_team_avg_age.csv", index="False")

master = master.merge(
    team_age,
    left_on=["Match ID", "H/A"],
    right_on=["Match ID", "Team Type"],
    how="left"
)

master.to_csv("208_dataset_AGE")