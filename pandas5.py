#pandas5.py

import pandas as pd
df = pd.read_csv('dirtydata.csv')
print(df.to_string())

#add 130 only in empty in Calories column
df["Calories"].fillna(130, inplace=True)
print(df.to_string())

#add 130 in empty cells within same dataframe 
df.fillna(130, inplace=True)
print(df.to_string())
