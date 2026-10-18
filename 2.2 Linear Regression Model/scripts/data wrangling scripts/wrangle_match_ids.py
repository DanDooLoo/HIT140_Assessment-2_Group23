import pandas as pd
import os

os.chdir(os.path.dirname(__file__))

df = pd.read_csv("team_level_dataset.csv")

df = df.sort_values("Match ID")

df.to_csv("team_level_dataset.csv", index=False)