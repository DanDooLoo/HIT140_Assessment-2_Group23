import pandas as pd
import os

os.chdir(os.path.dirname(__file__))

df = pd.read_csv("208_dataset_AGE.csv")

df = df.drop(columns=["index", "Team Type_x", "Team Type_y"])

df.to_csv("204_dataset_AGE2.csv", index=False)