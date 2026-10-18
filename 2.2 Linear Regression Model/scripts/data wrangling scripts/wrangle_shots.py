import pandas as pd
import os

os.chdir(os.path.dirname(__file__))

master = pd.read_csv("208_dataset_DLG.csv")
wc22 = pd.read_csv("WC22_players_shooting.csv")
wc26 = pd.read_csv("WC26_allplayers.csv")

wc22 = wc22[["Player", "Gls"]].copy()

# print(wc22.head())

# wc22.to_csv("test.csv", index=False)

wc26players_wc22shots = wc26.merge(
    wc22,
    on=["Player"],
    how="left"
)

# print(wc26players_wc22shots.head())

players_WC22PS = wc26players_wc22shots[["Match ID", "Team Type", "Player", "Gls_y"]].copy()

# print(players_WC22PS.head())

players_WC22PS["Gls_y"] = (
    players_WC22PS["Gls_y"].fillna(0)
)

team_wc22goals = (
    players_WC22PS
    .groupby(["Match ID", "Team Type"], as_index=False)["Gls_y"]
    .sum()
)

team_wc22goals = team_wc22goals.rename(
    columns={"Gls_y": "WC22GS",
             "Team Type": "H/A"}
)

# print(master.head())
# print(team_wc22goals.head())

master = master.merge(
    team_wc22goals,
    on=["Match ID", "H/A"],
    how="left"
)

print(master.head())
master.to_csv("208_dataset_WC22GS.csv", index=False)


"""
master = master.merge(
    mfp,
    left_on=["Match ID", "H/A"],
    right_on=["Match ID", "Team Type"],
    how="left"
)

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

master = master.drop(columns=["Team Type"])

master.to_csv("208_dataset_MFP.csv", index=False)
"""