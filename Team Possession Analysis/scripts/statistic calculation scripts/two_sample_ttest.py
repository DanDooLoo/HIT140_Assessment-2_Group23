import scipy.stats as st
import pandas as pd
import numpy as np

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

def two_ttest(sample1, sample2):

    x_bar1 = sample1.mean()
    s1 = sample1.std(ddof=1)
    n1 = len(sample1)

    x_bar2 = sample2.mean()
    s2 = sample2.std(ddof=1)
    n2 = len(sample2)

    t_stats, p_val = st.ttest_ind_from_stats(x_bar1, s1, n1, x_bar2, s2, n2, equal_var=False, alternative='two-sided')

    print("\n Computing t* ...")
    print("\t t-statistic (t*): %.3f" % t_stats)

    print("\n Computing p-value ...")
    print("\t p-value: %.4f" % p_val)

    print("\n Conclusion:")
    if p_val < 0.05:
        print("\t We reject the null hypothesis.")
    else:
        print("\t We accept the null hypothesis.")

two_ttest(h_fwd, l_fwd)