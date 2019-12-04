import numpy as np

a = np.array([[3, 2, 0], [1, -1, 0], [0, 5, 1]])
b = np.array([2, 4, -1])

from scipy import linalg

x = linalg.solve(a, b)
