import pandas as pd

df = pd.read_csv("team_composition.csv")

df["total"] = df["Defenders"] + df["Midfielders"] + df["Forwards"]

invalid_rows = df[df["total"].round(6) != 1]

if invalid_rows.empty:
    print("All rows sum to 1.")
else:
    print("Rows that do not sum 1:")
    print(invalid_rows)
