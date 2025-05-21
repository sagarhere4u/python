#pandas3.py
import pandas as pd

df = pd.read_csv("data.csv")

print(df)
print("===========================")
print(df.to_string())
print("===PRINT TOP 10 LINES======")
print(df.head(10))
print("===PRINT LAST 10 LINES======")
print(df.tail(10))
print("===PRINT INFO======")
print(df.info())


