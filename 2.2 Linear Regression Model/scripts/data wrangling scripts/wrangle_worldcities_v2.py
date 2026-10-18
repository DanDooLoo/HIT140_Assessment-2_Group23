import pandas as pd
import os

os.chdir(os.path.dirname(__file__))

cities = pd.read_csv("countries.csv")
city_coord = pd.read_csv("worldcities_clean.csv")

cities = cities.merge(
    city_coord[["City", "Country", "lat", "lng"]],
    on=["City", "Country"],
    how="left"
)

print(cities[["lat", "lng"]].isna().sum())

missing_cities = cities[
    cities["lat"].isna() |
    cities["lng"].isna()
    ]

print(missing_cities[["City", "Country"]])

cities = cities[["Country", "City", "lat", "lng"]].copy()

cities.to_csv("countries_clean.csv", index=False)

# print(df.head())
# df.to_csv("test.csv", index=False)