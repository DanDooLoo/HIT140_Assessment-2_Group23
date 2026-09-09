print ("Hello World")
import pandas as pd

import numpy as np


# Load CSV file into DataFrame

player_data = pd.read_csv('FIFA2026_player_stats.csv',encoding="latin-1")

match_team_data = pd.read_csv('match_team_stats.csv',encoding="latin-1")

matches_detailed_data = pd.read_csv('matches_detailed.csv',encoding="latin-1")

matches_summary_data = pd.read_csv('matches_summary.csv',encoding="latin-1")

teams_data = pd.read_csv('teams.csv',encoding="latin-1")

venues_data = pd.read_csv('venues.csv',encoding="latin-1")


# Display the DataFrame

print(player_data)
