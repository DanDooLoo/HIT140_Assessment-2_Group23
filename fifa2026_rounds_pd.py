import pandas as pd
import ast

# 1. Load CSV
df = pd.read_csv("rounds.csv")

# 2. Parse the JSON-like strings into Python objects
df["tournaments"] = df["tournaments"].apply(
    lambda x: ast.literal_eval(x) if isinstance(x, str) else None
)

# 3. Explode into match-level rows
matches = df.explode("tournaments").reset_index(drop=True)

# 4. Expand dict fields into columns
matches = pd.concat(
    [matches.drop(columns=["tournaments"]),
     matches["tournaments"].apply(pd.Series)],
    axis=1
)

# matches is now your clean match dataframe
print(matches.head())

# Columns are:
# id
# venueName
# venueCity
# venueId
# date
# homeSquadId
# awaySquadId
# homeSquadName
# awaySquadName
# homeScore
# awayScore
# groupName
# matchDay
# plus the round metadata (stage, roundName, etc.)
# All extracted cleanly from the CSV.

