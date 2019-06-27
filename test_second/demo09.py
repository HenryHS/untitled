import numpy as np
from sklearn.metrics import  mean_squared_error

t1 = np.arange(12).reshape(3, 4)

t2 = np.arange(4).reshape(4, 1)

t3 = t1.dot(t2)

print(t3)
