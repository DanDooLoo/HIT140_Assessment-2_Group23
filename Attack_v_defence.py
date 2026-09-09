import pandas as pd
import matplotlib.pyplot as plt

#Task 2 Effectiveness of attack and defense

# ------------------------------------------------------------
# 1. LOAD DATA
# ------------------------------------------------------------

team_stats = pd.read_csv("Match_team_stats.csv",encoding="latin-1" )
matches = pd.read_csv("Matches_summary.csv",encoding="latin-1" )

# ------------------------------------------------------------
# 2. EXTRACT HOME & AWAY CORNERS
# ------------------------------------------------------------

team_stats = team_stats.sort_values("match_id").reset_index(drop=True)

home = team_stats.groupby("match_id").nth(0).reset_index()
away = team_stats.groupby("match_id").nth(1).reset_index()

corners = pd.DataFrame({
    "match_id": home["match_id"],
    "corners_home": home["corners"],
    "corners_away": away["corners"]
})

# ------------------------------------------------------------
# 3. MERGE WITH MATCH SUMMARY
# ------------------------------------------------------------

df = matches.merge(corners, on="match_id")

# ------------------------------------------------------------
# 4. CALCULATE EFFICIENCY METRICS
# ------------------------------------------------------------

df["home_attack_eff"] = df["home_score"] / df["corners_home"]
df["away_attack_eff"] = df["away_score"] / df["corners_away"]

df["home_def_eff"] = 1 - (df["away_score"] / df["corners_home"])
df["away_def_eff"] = 1 - (df["home_score"] / df["corners_away"])

df = df.replace([float("inf"), -float("inf")], None)

# ------------------------------------------------------------
# 5. NUMERICAL SUMMARY
# ------------------------------------------------------------

summary = df[[
    "home_attack_eff",
    "away_attack_eff",
    "home_def_eff",
    "away_def_eff"
]].describe()

print("\n=== Efficiency Summary ===\n")
print(summary)

# ------------------------------------------------------------
# 6. GRAPHICAL REPRESENTATION
# ------------------------------------------------------------

# --- Scatter plots: Corners vs Goals ---
plt.figure(figsize=(12, 5))

plt.subplot(1, 2, 1)
plt.scatter(df["corners_home"], df["home_score"], alpha=0.7)
plt.xlabel("Home Corners")
plt.ylabel("Home Goals")
plt.title("Home: Corners vs Goals")

plt.subplot(1, 2, 2)
plt.scatter(df["corners_away"], df["away_score"], alpha=0.7, color="orange")
plt.xlabel("Away Corners")
plt.ylabel("Away Goals")
plt.title("Away: Corners vs Goals")

plt.tight_layout()
plt.show()

# --- Histograms: Attack Efficiency ---
plt.figure(figsize=(12, 5))

plt.subplot(1, 2, 1)
plt.hist(df["home_attack_eff"].dropna(), bins=20, alpha=0.7)
plt.xlabel("Home Attack Efficiency (Goals per Corner)")
plt.ylabel("Matches")
plt.title("Distribution of Home Attack Efficiency")

plt.subplot(1, 2, 2)
plt.hist(df["away_attack_eff"].dropna(), bins=20, alpha=0.7, color="orange")
plt.xlabel("Away Attack Efficiency (Goals per Corner)")
plt.ylabel("Matches")
plt.title("Distribution of Away Attack Efficiency")

plt.tight_layout()
plt.show()
