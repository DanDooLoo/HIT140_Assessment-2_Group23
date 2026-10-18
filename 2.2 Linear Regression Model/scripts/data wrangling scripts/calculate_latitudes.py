import pandas as pd
import os

os.chdir(os.path.dirname(__file__))

master = pd.read_csv("teams_dataset.csv")
countries = pd.read_csv("countries.csv")
venues = pd.read_csv("venues.csv")

master = master.merge(
    countries[["Country", "Country Latitude"]],
    left_on="Team",
    right_on="Country",
    how="left"
    )

master = master.merge(
    venues[["Venue", "Venue Latitude"]],
    on="Venue",
    how="left"
)

master = master.drop(columns="Country")

master.to_csv("204_data_set_lats.csv", index=False)