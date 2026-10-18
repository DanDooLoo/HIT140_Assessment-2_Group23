import os
import pandas as pd
import statsmodels.api as sm
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib
from sklearn.metrics import mean_squared_error

os.chdir(os.path.dirname(__file__))

df = pd.read_csv('208_model_dataset.csv')

# seperating explanatory variables and the response variable
x = df[
    [
        'LDIF',
        'AGE',
        'MFP',
        'DLG',
        'RP',
        'WC22SOT'
    ]
]

y = df['Goals']

# building the linear regression model
x = sm.add_constant(x)
model = sm.OLS(y,x).fit()
pred = model.predict(x)
model_details = model.summary()
print(model_details)

rmse = np.sqrt(mean_squared_error(y, pred))

nrmse = rmse / (y.max() - y.min())

print('RMSE:', rmse)
print('NRMSE:', nrmse)

"""
residuals = y - pred

plt.figure(figsize=(7,5))

sns.scatterplot(x=pred, y=residuals)
plt.axhline(y=0, color='red', linestyle='--')

plt.xlabel('Predicted Goals')
plt.ylabel('Residuals')
plt.title('Residuals vs Predicted Goals')

plt.tight_layout()
plt.show()

print("Backend: ", matplotlib.get_backend())
print("Interactive: ", plt.isinteractive())

"""
"""
plt.plot([1, 2, 3], [1, 4, 9])
plt.title('Test Plot')
"""