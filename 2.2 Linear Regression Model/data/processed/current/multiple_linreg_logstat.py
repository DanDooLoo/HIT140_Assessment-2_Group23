import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.api as sm
import numpy as np

# Read dataset into a DataFrame
df = pd.read_csv("boston.csv")

# Separate explanatory variables (x) from the response variable (y)
x = df.iloc[:,:-1]
y = df.iloc[:,-1]

# Build and evaluate the linear regression model
x = sm.add_constant(x)
model = sm.OLS(y,x).fit()
pred = model.predict(x)
model_details = model.summary()
print(model_details)


"""Non-linear transformation of LSTAT variable"""

# Re-read dataset into a DataFrame
df = pd.read_csv("boston.csv")

# Apply non-linear transformation
df["LOGSTAT"] = df["LSTAT"].apply(np.log)

# Rearrange the variables so that MV appears as the last column
df = df[['CRIM','ZN','INDUS','CHAS','NOX','RM','AGE','DIS','RAD','TAX','PTRATIO','LSTAT','LOGSTAT','MV']]

# Visualise the effect of the transformation
plt.figure(figsize=(20,10))

plt.subplot(1,2,1)
plt.scatter(df["LSTAT"], df["MV"], color="green")
plt.title("Original LSTAT")
plt.xlabel("LSTAT")
plt.ylabel("MV")
plt.plot([0,40],[30,0])

plt.subplot(1,2,2)
plt.scatter(df["LOGSTAT"], df["MV"], color="red")
plt.title("Log Transformed LSTAT")
plt.xlabel("LOGSTAT")
plt.ylabel("MV")
plt.plot([0,4],[50,0])

plt.show()


"""
RE-RUN THE LINEAR REGRESSION MODEL WITH A TRANSFORMED VARIABLE
"""
# Drop the original LSTAT variable
df = df.drop("LSTAT", axis=1)

# Separate explanatory variables (x) from the response variable (y)
x = df.iloc[:,:-1]
y = df.iloc[:,-1]

# Build and evaluate the linear regression model
x = sm.add_constant(x)
model = sm.OLS(y,x).fit()
pred = model.predict(x)
model_details = model.summary()
print(model_details)


"""
SINCE LOGSTAT WORKS BETTER THAN LSTAT FOLLOWING THE LINEAR TRANSFORMATION:
1. WRITE THE TRANSFORMED DATAFRAME INTO A .CSV FILE
2. RE-RUN THE LINEAR REGRESSION MODEL USING SKLEARN
"""

# # write dataframe to .csv
# df.to_csv("boston_logstat.csv", index=False)
