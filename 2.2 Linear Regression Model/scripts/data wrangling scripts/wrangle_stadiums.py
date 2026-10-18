import pandas as pd
import os

os.chdir(os.path.dirname(__file__))

df = pd.read_csv("teams_dataset.csv")

df[["Venue"]].drop_duplicates().to_csv("venues.csv", index=False)