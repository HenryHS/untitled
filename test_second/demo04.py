import pandas as pd
import numpy as np

p = pd.Series(data=[1,2,3], index=list('abc'), dtype=np.float64, name='title')

print(p, type(p), p.index, p.dtype, p.values)

df = pd.DataFrame(data=np.arange(12).reshape(3,4), index=list('abc'), columns=list('wxyz'), dtype=np.float16)

print(df,type(df))

print(df.index,type(df.index))

print(df.columns,type(df.columns))

print(df.values,type(df.values))

print(df.dtypes)