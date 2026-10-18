import pandas as pd
import os

os.chdir(os.path.dirname(__file__))

wc22_players = pd.read_csv("WC22_players.csv")
wc26_players = pd.read_csv("WC26_allplayers.csv")
wc22_lookup = wc22_players[["Player", "WC22 Minutes"]].copy()
master = pd.read_csv("208_dataset_LDIF.csv")

players_exp = wc26_players.merge(
    wc22_lookup,
    on="Player",
    how="left"
)

players_exp["WC22 Minutes"] = (
    players_exp["WC22 Minutes"].fillna(0)
)

# players_exp.to_csv("WC26_allplayers_exp.csv", index=False)

team_exp = (
    players_exp
    .groupby(["Match ID", "Team Type"], as_index=False)["WC22 Minutes"]
    .sum()
)

team_exp["Team Type"] = team_exp["Team Type"].replace({
    "home": "Home",
    "away": "Away"
})

team_exp = team_exp.rename(
    columns={
        "WC22 Minutes": "WC22XP"
    }
)

# team_exp.to_csv("WC26_team_exp.csv", index=False)

master = master.merge(
    team_exp,
    left_on=["Match ID", "H/A"],
    right_on=["Match ID", "Team Type"],
    how="left"
)

master.to_csv("208_dataset_WC22XP.csv", index=False)