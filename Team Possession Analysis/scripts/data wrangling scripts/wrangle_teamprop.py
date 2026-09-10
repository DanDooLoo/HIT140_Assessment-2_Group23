import pandas as pd
import glob
import os

POSITION_MAP = {
    "CB": "DF", "LB": "DF", "RB": "DF", "FB": "DF", "DF": "DF",

    "CM": "MF", "DM": "MF", "AM": "MF", "MF": "MF",
    "LM": "MF", "RM": "MF", "WM": "MF",

    "LW": "FW", "RW": "FW", "FW": "FW",

    "GK": "GK"
}

# --- PATHS ---
BASE_DIR = os.path.dirname(os.path.abspath(__file__))  # fbref_data/processed/current/
RAW_DIR = os.path.join(BASE_DIR, "..", "..", "raw", "teams")  # fbref_data/raw/teams/

MATCHES_PATH = os.path.join(BASE_DIR, "match_list_with_ids.csv")       # fbref_data/raw/teams/match.csv
PLAYER_DATA_DIR = RAW_DIR                               # folder containing match_XXX_home.csv etc.

# --- READ MATCH LIST CSV ---
matches_df = pd.read_csv(MATCHES_PATH)   # Column: Match ID
match_ids = matches_df["Match ID"].astype(str).tolist()

all_frames = []

match_ids = (
    matches_df["Match ID"]
    .astype(int)
    .astype(str)
    .str.zfill(3)
    .tolist()
)

for mid in match_ids:
    pattern = os.path.join(PLAYER_DATA_DIR, f"match_{mid}_*.csv")
    files = glob.glob(pattern)

    for file in files:
        df = pd.read_csv(file)

        # Columns read from player CSV:
        # Pos — Player position(s)
        # Player Name — Player name
        # Minutes Played — Minutes played in the match
        # (Add comments for any other columns you have)

        basename = os.path.basename(file)
        _, match_id, team_type = basename.replace(".csv", "").split("_")

        df["Match ID"] = match_id
        df["Team Type"] = team_type

        all_frames.append(df)

players = pd.concat(all_frames, ignore_index=True)

# --- TEAM COMPOSITION CALCULATION ---

def compute_role_weights(pos_string):
    """
    Convert Pos string into fractional weights.
    Uses POSITION_MAP to mask detailed roles.
    Excludes GK entirely.
    """
    if pd.isna(pos_string):
        return {"DF": 0, "MF": 0, "FW": 0, "is_outfielder": False}

    raw_roles = [r.strip() for r in pos_string.split(",")]

    mapped_roles = [POSITION_MAP.get(r, None) for r in raw_roles]

    roles = [r for r in mapped_roles if r in ("DF", "MF", "FW")]

    if len(roles) == 0:
        return {"DF": 0, "MF": 0, "FW": 0, "is_outfielder": False}

    weight = 1 / len(roles)

    return {
        "DF": weight if "DF" in roles else 0,
        "MF": weight if "MF" in roles else 0,
        "FW": weight if "FW" in roles else 0,
        "is_outfielder": True
    }

role_weights = players["Pos"].apply(compute_role_weights)
role_df = pd.DataFrame(role_weights.tolist())

players = pd.concat([players, role_df], axis=1)

# Only outfield players count toward denominator
outfielders = players[players["is_outfielder"]]

# Sum fractional weights per team
composition = (
    outfielders.groupby(["Match ID", "Team Type"])[["DF", "MF", "FW"]]
    .sum()
    .reset_index()
)

# Count outfield players per team
team_sizes = (
    outfielders.groupby(["Match ID", "Team Type"])
    .size()
    .reset_index(name="Outfield Players")
)

composition = composition.merge(team_sizes, on=["Match ID", "Team Type"])

# Normalised proportions (sum to 1)
composition["Defenders"] = composition["DF"] / composition["Outfield Players"]
composition["Midfielders"] = composition["MF"] / composition["Outfield Players"]
composition["Forwards"] = composition["FW"] / composition["Outfield Players"]

final_team_composition = composition[[
    "Match ID", "Team Type",
    "Defenders", "Midfielders", "Forwards"
]]

# --- WRITE OUTPUT CSV ---
OUTPUT_PATH = os.path.join(BASE_DIR, "team_composition.csv")
final_team_composition.to_csv(OUTPUT_PATH, index=False)

print(f"Saved team composition to: {OUTPUT_PATH}")


