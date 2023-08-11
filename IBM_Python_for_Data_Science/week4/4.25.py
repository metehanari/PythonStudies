#numpy two dimensional arrays

import numpy as np

a = [[11, 12, 13], [21, 22, 23], [31, 32, 33]]
# a is a nested list

A = np.array(a)
# A is a numpy array

print(A)

print(A.ndim)
# print the number of dimensions of A

print(A.shape)
# print the shape of A