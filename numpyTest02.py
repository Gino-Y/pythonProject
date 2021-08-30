import numpy as np


x = np.arange(27)
print(x)
x = np.reshape(x, (3,3,3))
print('(行，列， 通道)', x.shape)
print(x)
print('第0个水平面', x[0])
print('变成 a ', x[0][0])
