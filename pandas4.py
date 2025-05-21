#pandas4.py

import pandas as pd
df = pd.read_csv('dirtydata.csv')
print(df.to_string())
#create new df with rows having empty cell being removed
new_df = df.dropna()
print(new_df.to_string())

#removes rows having empty cell in existing dataframe
df.dropna(inplace=True)
print(df.to_string())