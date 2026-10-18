import pandas as pd
import numpy as np

df = pd.read_csv("composition_and_possession.csv")

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

print("high defender mean: %.3f" % (h_def.mean()),
      "\nhigh defender median: %.3f" % (h_def.median()),
      "\nhigh defender std: %.3f" % (h_def.std(ddof=1)),
      "\nhigh defender min: %.3f" % (np.min(h_def)),
      "\nhigh defender max: %.3f" % (np.max(h_def)),
      "\nhigh defender pct25: %.3f" % (np.percentile(h_def, 25)),
      "\nhigh defender pct75: %.3f" % (np.percentile(h_def, 75)),
      "\nhigh defender IQR: %.3f" % (np.percentile(h_def, 75) - np.percentile(h_def, 25)),
      "\nhigh defender count: %.3f" % (len(h_def)))

print("low defender mean: %.3f" % (l_def.mean()),
      "\nlow defender median: %.3f" % (l_def.median()),
      "\nlow defender std: %.3f" % (l_def.std(ddof=1)),
      "\nlow defender min: %.3f" % (np.min(l_def)),
      "\nlow defender max: %.3f" % (np.max(l_def)),
      "\nlow defender pct25: %.3f" % (np.percentile(l_def, 25)),
      "\nlow defender pct75: %.3f" % (np.percentile(l_def, 75)),
      "\nlow defender IQR: %.3f" % (np.percentile(l_def, 75) - np.percentile(l_def, 25)),
      "\nlow defender count: %.3f" % (len(l_def)))

print("high mid mean: %.3f" % (h_mid.mean()),
      "\nhigh mid median: %.3f" % (h_mid.median()),
      "\nhigh mid std: %.3f" % (h_mid.std(ddof=1)),
      "\nhigh mid min: %.3f" % (np.min(h_mid)),
      "\nhigh mid max: %.3f" % (np.max(h_mid)),
      "\nhigh mid pct25: %.3f" % (np.percentile(h_mid, 25)),
      "\nhigh mid pct75: %.3f" % (np.percentile(h_mid, 75)),
      "\nhigh mid IQR: %.3f" % (np.percentile(h_mid, 75) - np.percentile(h_mid, 25)),
      "\nhigh mid count: %.3f" % (len(h_mid)))

print("low mid mean: %.3f" % (l_mid.mean()),
      "\nlow mid median: %.3f" % (l_mid.median()),
      "\nlow mid std: %.3f" % (l_mid.std(ddof=1)),
      "\nlow mid min: %.3f" % (np.min(l_mid)),
      "\nlow mid max: %.3f" % (np.max(l_mid)),
      "\nlow mid pct25: %.3f" % (np.percentile(l_mid, 25)),
      "\nlow mid pct75: %.3f" % (np.percentile(l_mid, 75)),
      "\nlow mid IQR: %.3f" % (np.percentile(l_mid, 75) - np.percentile(l_mid, 25)),
      "\nlow mid count: %.3f" % (len(l_mid)))

print("high fwd mean: %.3f" % (h_fwd.mean()),
      "\nhigh fwd median: %.3f" % (h_fwd.median()),
      "\nhigh fwd std: %.3f" % (h_fwd.std(ddof=1)),
      "\nhigh fwd min: %.3f" % (np.min(h_fwd)),
      "\nhigh fwd max: %.3f" % (np.max(h_fwd)),
      "\nhigh fwd pct25: %.3f" % (np.percentile(h_fwd, 25)),
      "\nhigh fwd pct75: %.3f" % (np.percentile(h_fwd, 75)),
      "\nhigh fwd IQR: %.3f" % (np.percentile(h_fwd, 75) - np.percentile(h_fwd, 25)),
      "\nhigh fwd count: %.3f" % (len(h_fwd)))

print("low fwd mean: %.3f" % (l_fwd.mean()),
      "\nlow fwd median: %.3f" % (l_fwd.median()),
      "\nlow fwd std: %.3f" % (l_fwd.std(ddof=1)),
      "\nlow fwd min: %.3f" % (np.min(l_fwd)),
      "\nlow fwd max: %.3f" % (np.max(l_fwd)),
      "\nlow fwd pct25: %.3f" % (np.percentile(l_fwd, 25)),
      "\nlow fwd pct75: %.3f" % (np.percentile(l_fwd, 75)),
      "\nlow fwd IQR: %.3f" % (np.percentile(l_fwd, 75) - np.percentile(l_fwd, 25)),
      "\nlow fwd count: %.3f" % (len(l_fwd)))