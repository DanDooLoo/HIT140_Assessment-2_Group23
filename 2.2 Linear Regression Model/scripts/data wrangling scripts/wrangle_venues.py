import pandas as pd
import os

os.chdir(os.path.dirname(__file__))

teams_df = pd.read_csv("team_level_dataset.csv")
master_df = pd.read_csv("match_list_no_penalties.csv")

teams_df = teams_df.merge(
    master_df[["Match ID", "Venue"]],
    on="Match ID",
    how="left"
)

teams_df.to_csv("teams_dataset.csv", index=False)

print(teams_df["Venue"].isna().sum())