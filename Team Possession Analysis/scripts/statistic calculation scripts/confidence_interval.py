import pandas as pd
import statsmodels.stats.weightstats as stm
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


def ci(sample, alpha=0.05):
    mean = sample.mean()
    sd = sample.std(ddof=1)
    n = len(sample)

    ci_low, ci_upp = stm._zconfint_generic(
        mean, sd / math.sqrt(n),
        alpha=alpha,
        alternative='two-sided'
    )
    print(f"{ci_low:.3f}", f"{sample.mean():.3f}", f"{ci_upp:.3f}")

ci(h_fwd)