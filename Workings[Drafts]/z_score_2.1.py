import pandas as pd
import statsmodels.api as sm
from sklearn.preprocessing import StandardScaler

df = pd.read_csv("L_R_2.1.csv")

x = df.iloc[:,:-1]
y = df.iloc[:,-1]

# Build the linear regression 
x = sm.add_constant(x)
model = sm.OLS(y,x).fit()
model.predict(x)
model_report = model.summary()
print(model_report)

# Apply Standardisation

scaler = StandardScaler()
x = x.drop(['const'], axis=1)

std_x = scaler.fit_transform(x.values)

std_x_df = pd.DataFrame(std_x, index=x.index, columns=x.columns)

std_x_df = sm.add_constant(std_x_df)
model = sm.OLS(y,std_x_df).fit()
pred = model.predict(std_x_df)
model_report = model.summary()
print(model_report)