#%%
# this is the introduction to numpy

import numpy as np

# x = 2
# print(x)
#
# y = x ** 2
#
# print(y)
#
# var = np.__version__
#
# print(var)
#
# /* C */
# int result = 0;
# for (int i = 0; i < 100; i++) {
#     result =+= i;
# }


# Python Code

# result = 0
# for i in range(100):
#     result += 1
#     print(result)
#
# np.random.seed(0) # seed for reproducibility

x1 = np.random.randint(10, size=6) #One dimensional array
x2 = np.random.randint(10, size=(3,4)) #Two dim array
x3 = np.random.randint(10, size=(3,4,5)) #Three dim array
# print(x2)
# print(x3)
#
# print("x3 ndim: ", x3.ndim)
# print("x3 shape: ", x3.shape)
# print("x3 size: ", x3.size)
# print("dtype: ", x3.dtype)
# print("itemsize: ", x3.itemsize, "bytes")
# print("nbytes: ", x3.nbytes, "bytes")

x = np.arange(11)
# print(x)
# print(x[:5])
# print(x[5:])
# print(x[4:7])
# print(x[::2])
# print(x[1::2])

# print(x2)
x2_sub = x2[:2, :2]
# print(x2_sub)
# Question retarding the x2_subarray
#
x2_sub[0,0] = 99
# print(x2_sub)
# print(x2)
#
x2_sub_copy = x2[:2, :2].copy()
# print(x2_sub_copy)

x2_sub_copy[0,0] = 42
# print(x2_sub_copy)
# print(x2)

grid = np.arange(1,10).reshape((3,3))
# print(grid)

x = np.array([1,2,3])
x.reshape((1,3))
# print(x.reshape(1,3))

# print(x[:, np.newaxis])

x = np.array([1,2,3])
y = np.array([3,4,5])
z = [99, 99, 99]
# print(np.concatenate([x,y,z]))

grid = np.array([[1,2,3],
                [4,5,6]])
# print(np.concatenate([grid, grid]))

# print(np.concatenate([grid, grid], axis= 1))

x = np.array([1,2,3])
grid = np.array([[9,8,7],[6,5,4]])

# print(np.vstack([x, grid]))

y = np.array([[99],
              [99]])
# print(np.hstack([grid,y]))

x = [1,2,3,99,99,3,2,1]
x1, x2, x3 = np.split(x, [3,5])
# print(x1, x2, x3)

grid = np.arange(16).reshape((4,4))
# print(grid)

upper, lower = np.vsplit(grid, [2])
# print(upper)
# print(lower)

left, right = np.hsplit(grid, [2])
print(left)
print(right)

#%% computation on numpy arrays

import numpy as np
from datetime import datetime
np.random.seed(0)

def compute_recipricals(values):
    output = np.empty(len(values))
    for i in range(len(values)):
        output[i] = 1.0 / values[i]
    return output

values = np.random.randint(1, 10, size=5)
# print(values)
# print(compute_recipricals(values))

import timeit
big_array = np.random.randint(1, 100, size = 10000000) # how about a vector of sizes
# print(timeit(compute_recipricals(big_array))) #This is a jupyter command, not helpful for pycharm
start = datetime.now()
compute_recipricals(big_array)
finish = datetime.now() - start
# print(finish) # check it for several sizes to make sure it works

#%%% Introducing UFuncs

# print(compute_recipricals(values))
# print(1/values)

# ?timeit # why this funciton doesn't work

# print(np.arange(5)/np.arange(1,6))

x = np.arange(9).reshape((3,3))
print(2**x)

#%% Start from Array arithmetic


