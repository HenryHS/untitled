import pandas as pd

df = pd.read_csv('../data/groupby.csv')

# df.info()

# print(df.head(n=3))

dt = df.sort_values(by='Count', ascending=True)

dg = df.groupby(by='Brand').sum()

print(dg, type(dg))

# for i, v in dg:
#     print(i, type(i))
#     print(v, type(v))
