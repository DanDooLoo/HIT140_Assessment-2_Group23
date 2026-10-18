import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("composition_and_possession.csv")

high = df[df["Possession"] >= 0.65]
low  = df[df["Possession"] <= 0.35]

h_def = high["Defenders"]
l_def = low["Defenders"]

h_mid = high["Midfielders"]
l_mid = low["Midfielders"]

h_fwd = high["Forwards"]
l_fwd = low["Forwards"]

plt.boxplot([h_def, l_def], label=["Low possession", "High possession"], patch_artist=True, boxprops=dict(facecolor="#8ecae6"))
plt.title("Defender Proportion by Possession Group")
plt.ylabel("Defender Proportion")
plt.show()

plt.boxplot([h_mid, l_mid], label=["Low possession", "High possession"], patch_artist=True, boxprops=dict(facecolor="#c68ee6"))
plt.title("Midfielder Proportion by Possession Group")
plt.ylabel("Midfielder Proportion")
plt.show()

plt.boxplot([h_fwd, l_fwd], label=["Low possession", "High possession"], patch_artist=True, boxprops=dict(facecolor="#e06fa0"))
plt.title("Forward Proportion by Possession Group")
plt.ylabel("Forward Proportion")
plt.show()

