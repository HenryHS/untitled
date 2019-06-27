import numpy as np
import random

t1 = np.arange(12)

l = [[1,2,3],[4,5,6],[7,8,'123']]

t2 = np.array(l)

t3 = np.random.randint()

print(t3, type(t3), t3.shape,t3.dtype)

t1 = t1.reshape(3, 4)

# print(t1.dtype, t1.shape, t1.size, t1.itemsize)
