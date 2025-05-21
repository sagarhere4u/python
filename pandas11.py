#pandas11.py
import sys
import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('pandasdata.csv')

for x in df.index:
  if df.loc[x, "Income"] < 5000:
    df.drop(x, inplace=True)

df['Sex'].value_counts().plot.bar(color=["orange", "blue"], width=.3)

plt.show()

#Two  lines to make our compiler able to draw:
plt.savefig(sys.stdout.buffer)
sys.stdout.flush()