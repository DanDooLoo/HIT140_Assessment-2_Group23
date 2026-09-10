import matplotlib.pyplot as plt
import numpy as np
import statsmodels.stats.weightstats as stm
import pandas as pd
import math

df = pd.read_csv("composition_and_possession.csv")

high = df[df["Possession"] >= 0.65]
low  = df[df["Possession"] <= 0.35]

h_def = high["Defenders"]
l_def = low["Defenders"]

h_mid = high["Midfielders"]
l_mid = low["Midfielders"]

h_fwd = high["Forwards"]
l_fwd = low["Forwards"]

low_n = 32
high_n = 33

def ci_halfwidth(sample, alpha=0.05):
    mean = sample.mean()
    sd = sample.std(ddof=1)
    n = len(sample)

    ci_low, ci_upp = stm._zconfint_generic(
        mean,
        sd / math.sqrt(n),
        alpha=alpha,
        alternative='two-sided'
    )

    half_width = (ci_upp - ci_low) / 2

    return half_width

roles = ["Defenders", "Midfielders", "Forwards"]

x = np.array([0, 1.4, 2.8])
width = 0.25

means_low = [l_def.mean(), l_mid.mean(), l_fwd.mean()]
means_high = [h_def.mean(), h_mid.mean(), h_fwd.mean()]

ci_low = [ci_halfwidth(l_def), ci_halfwidth(l_mid), ci_halfwidth(l_fwd)]
ci_high = [ci_halfwidth(h_def), ci_halfwidth(h_mid), ci_halfwidth(h_fwd)]

plt.figure(figsize=(8,5))

plt.bar(x - width/1.5, means_high, width, yerr=ci_high, capsize=5, label="High possession", color="#8ecae6")
plt.bar(x + width/1.5, means_low,  width, yerr=ci_low,  capsize=5, label="Low possession", color="#e06fa0")

plt.xticks(x, roles)
plt.ylabel("Proportion")
plt.title("Mean Role Proportions ± 95% CI")
plt.legend()

plt.show()