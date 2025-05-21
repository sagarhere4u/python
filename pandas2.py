#pandas2.py
import pandas as pd

data = {
    'calories': [100,200,300],
    'duration': [10,20,30]
}

df = pd.DataFrame(data)
print(df)
print(df.loc[1])
