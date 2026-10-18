import pandas as pd
import os

os.chdir(os.path.dirname(__file__))

df = pd.read_csv("team_level_dataset.csv")

df[["Team"]].drop_duplicates().to_csv("countries.csv", index=False)