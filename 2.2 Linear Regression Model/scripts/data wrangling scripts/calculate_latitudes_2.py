import pandas as pd
import os

os.chdir(os.path.dirname(__file__))

df = pd.read_csv("204_data_set_lats.csv")

df["LDIF"] = (
    df["Country Latitude"] - df["Venue Latitude"]
).abs()

df = df.drop(columns=["Country Latitude", "Venue Latitude"])

df.to_csv("204_dataset_LDIF.csv", index=False)