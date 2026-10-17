import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn import metrics
import seaborn as sns
import matplotlib.pyplot as plt
import math
import numpy as np

# Load data files
attempts = pd.read_csv("attempts_at_goal_team.csv")
fifa_stats = pd.read_csv("FIFA_Site_Team_Stats.csv")
rounds2026 = pd.read_csv("rounds2026.csv")

# Inspect data structure and quality
attempts.info()
fifa_stats.info()
rounds2026.info()

# Standardise column names for consistency
attempts_renamed = attempts.rename(columns={
    "team": "Team",
    "team_abbrv": "TeamAbbr",
    "goals": "Goals",
    "assists": "Assists",
    "attempt_at_goal": "Attempts_at_goal",
    "attempt_ontarget": "Attempts_on_target",
    "offtarget_attempt": "Off_Target_Attempts",
    "attempt_goal_convRate_percentage": "Attempts_at_goal_conversionrate(%)",
    "attempt_inside_pa": "Attempts_Inside_PenaltyArea",
    "attempt_outside_pa": "Attemps_Outside_PenaltyArea",
    "headed_attempt_goal": "Headed_Attemps_at_Goal",
    "xG": "xG",
    "xG_efficiency": "xG_Efficiency",
    "corners": "Corners",
    "possession_control_percentage": "Possession_Control(%)"
})

team_stats = attempts_renamed.copy()

# Keep only matches with complete score data
matches = rounds2026.dropna(subset=["homeScore", "awayScore"].copy())

matches.head()
matches.info()

print("Number of matches with scores: ", len(matches))

matches_len = len(matches)
matches["goal_diff"] = matches["homeScore"] - matches["awayScore"]

# Merge match data with home team statistics
home = matches.merge(
    team_stats,
    left_on="homeSquadAbbr",
    right_on="TeamAbbr",
    how="left",
    suffixes=("", "_home")
)

# Visualize shooting accuracy: attempts vs goals scored
plt.figure(figsize=(10, 6))

sns.scatterplot(
    x=home["Attempts_at_goal"],
    y=home["Goals"],
    color="blue",
    s=80,
    edgecolor="black",
    label="Attempts at Goal"
)

sns.scatterplot(
    x=home["Attempts_on_target"],
    y=home["Goals"],
    color="green",
    s=80,
    edgecolor="black",
    label="Attempts on Target"
)

sns.regplot(
    x=home["Attempts_at_goal"],
    y=home["Goals"],
    scatter=False,
    line_kws={"color": "red", "linewidth": 2},
    label="Goals Trendline"
)

plt.xlabel("Attempts")
plt.ylabel("Goals")
plt.title("Attempts at Goal vs Attempts on Target")
plt.legend()
plt.show()

# Prefix home team columns to distinguish from away team
home_cols_map = {
    "Goals": "home_Goals",
    "Attempts_at_goal": "home_Attempts_at_goal",
    "Attempts_on_target": "home_Attempts_on_target",
    "Attempts_at_goal_conversionrate(%)": "home_ConversionRate",
    "Attempts_Inside_PenaltyArea": "home_Attempts_inside_PA",
    "Headed_Attemps_at_Goal": "home_Headed_attempts",
    "xG": "home_xG",
    "Possession_Control(%)": "home_Possession",
    "xG_Efficiency_num": "home_xG_eff"
}
home.rename(columns=home_cols_map, inplace=True)

# Merge away team statistics to create full match dataset
full = home.merge(
    team_stats,
    left_on="awaySquadAbbr",
    right_on="TeamAbbr",
    how="left",
    suffixes=("", "_away")
)

# Prefix away team columns
away_cols_map = {
    "Goals": "away_Goals",
    "Attempts_at_goal": "away_Attempts_at_goal",
    "Attempts_on_target": "away_Attempts_on_target",
    "Attempts_at_goal_conversionrate(%)": "away_ConversionRate",
    "Attempts_Inside_PenaltyArea": "away_Attempts_inside_PA",
    "Headed_Attemps_at_Goal": "away_Headed_attempts",
    "xG": "away_xG",
    "Possession_Control(%)": "away_Possession",
    "xG_Efficiency_num": "away_xG_eff"
}
full.rename(columns=away_cols_map, inplace=True)

# Create difference features (home minus away) to capture home team advantage
full["diff_goals_scored"] = full["home_Goals"] - full["away_Goals"]
full["diff_attempts_at_goal"] = full["home_Attempts_at_goal"] - full["away_Attempts_at_goal"]
full["diff_attempts_on_target"] = full["home_Attempts_on_target"] - full["away_Attempts_on_target"]
full["diff_conversion_rate"] = full["home_ConversionRate"] - full["away_ConversionRate"]
full["diff_attempts_inside_pa"] = full["home_Attempts_inside_PA"] - full["away_Attempts_inside_PA"]
full["diff_headed_attempts"] = full["home_Headed_attempts"] - full["away_Headed_attempts"]
full["diff_xG"] = full["home_xG"] - full["away_xG"]
full["diff_possession"] = full["home_Possession"] - full["away_Possession"]

feature_cols = [
    "diff_goals_scored",
    "diff_attempts_at_goal",
    "diff_attempts_on_target",
    "diff_conversion_rate",
    "diff_attempts_inside_pa",
    "diff_headed_attempts",
    "diff_xG",
    "diff_possession"
]

full.head()

