import pandas as pd
import os

os.chdir(os.path.dirname(__file__))

df = pd.read_csv("worldcities.csv")


for col in ["city", "country"]:
    df[col] = df[col].str.strip('"').str.strip()

print(df.head())
df.to_csv("test.csv", index=False)