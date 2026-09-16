import pandas as pd

teamcomp_df = pd.read_csv("team_composition.csv")
matchlist_df = pd.read_csv("match_list_with_ids.csv")

matchlist_df = matchlist_df[["Match ID", "Home Possession", "Away Possession"]]

merged = teamcomp_df.merge(matchlist_df, on="Match ID")

merged["Proportion"] = merged["Home Possession"].where(
    merged["Team Type"] == "home",
    merged["Away Possession"]
)

merged = merged.drop(columns=["Home Possession", "Away Possession"])

merged.to_csv("composition_and_possession.csv", index=False)

print(merged.head)