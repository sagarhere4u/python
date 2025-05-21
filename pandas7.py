#pandas7.py

import pandas as pd

df = pd.read_csv("dirtydata.csv")

#deleting duplicate rows in dataframe
df.drop_duplicates(inplace=True)

print(df.to_string())