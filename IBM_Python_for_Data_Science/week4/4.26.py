# numpy vector multipications

import numpy as np

a = np.array([[1, 2],[3, 4]])

b = np.array([[1, 0], [0, 1]])

print(a * b)
# Hadamard product. This is not matrix multiplication

print(np.dot(a, b)) 
# Matrix multiplication