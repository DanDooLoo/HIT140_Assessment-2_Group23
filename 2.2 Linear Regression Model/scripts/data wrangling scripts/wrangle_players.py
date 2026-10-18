import pandas as pd
import glob
import os

# --- PATHS ---
BASE_DIR = os.path.dirname(os.path.abspath(__file__))  # fbref_data/processed/current/
RAW_DIR = os.path.join(BASE_DIR, "..", "..", "raw", "teams")  # fbref_data/raw/teams/

MATCHES_PATH = os.path.join(BASE_DIR, "match_list_no_penalties.csv")       # fbref_data/raw/teams/match.csv
PLAYER_DATA_DIR = RAW_DIR                        # folder containing match_XXX_home.csv etc.

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


# print(len(all_frames))
# print(len(files))
players = pd.concat(all_frames, ignore_index=True)
print(players.info())
players.to_csv("WC26_allplayers.csv", index=False)