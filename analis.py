import pandas as pd

df = pd.read_csv('Car data.csv')
print(df.head())
print(df.info())
print(df.describe())

df1 = pd.read_csv('dz.csv')
df1.fillna(0, inplace=True)
print(df1['Salary'].mean)