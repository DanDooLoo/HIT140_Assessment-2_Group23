import pandas as pd
import os

os.chdir(os.path.dirname(__file__))

wc26_players = pd.read_csv("WC26_allplayers_old.csv")

wc26_players["Team Type"] = wc26_players["Team Type"].replace({
    "home": "Home",
    "away": "Away"
})

wc26_players.to_csv("WC26_allplayers.csv")