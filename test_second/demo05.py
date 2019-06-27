import pandas as pd

df = pd.read_csv('../data/groupby.csv')

df.info()

print(df.head(n=3))