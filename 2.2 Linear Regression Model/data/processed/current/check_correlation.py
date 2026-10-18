import os
import pandas as pd
import statsmodels.api as sm
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

os.chdir(os.path.dirname(__file__))

df = pd.read_csv('208_model_dataset.csv')

variables = [
    'LDIF',
    'AGE',
    'MFP',
    'DLG',
    'RP',
    'WC22XP',
    'WC22GS',
    'WC22SOT'
]
"""
for var in variables:
    sns.regplot(data=df, x=var, y='Goals')
    plt.title(f'{var} vs Goals')
    plt.show()

"""

# sns.histplot(data=df, x='AGE', kde=True)

sns.histplot(df['WC22SOT'], kde=True)
plt.title('Distribution of shots on target')
plt.show()