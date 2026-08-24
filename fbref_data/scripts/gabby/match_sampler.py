import pandas as pd

match_df = pd.read_csv("FBRef_match_list.csv")

group_stage_df = match_df[match_df["Round"] == "Group stage"]
knockout_stage_df = match_df[match_df["Round"] != "Group stage"]