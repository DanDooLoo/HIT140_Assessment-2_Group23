import pandas as pd
import os

os.chdir(os.path.dirname(__file__))

master = pd.read_csv("208_dataset_final.csv")

model_df = master[[
    "Goals",
    "LDIF",
    "AGE",
    "MFP",
    "DLG",
    "RP",
    "WC22XP",
    "WC22GS",
    "WC22SOT"
]].copy()

model_df["RP"] = (
    model_df["RP"].fillna(0)
)

model_df.to_csv("208_model_dataset.csv", index=False)