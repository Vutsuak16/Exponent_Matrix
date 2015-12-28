import numpy as np
from numpy import linalg as LA

a = np.array([[0, 1, 0, 0, 0, 0], [0, 0, 1, 0, 0, 0], [0, 0, 0, 1, 0, 0], [0, 0, 0, 0, 1, 0], [0, 0, 0, 0, 0, 1],
              [1, 1, 1, 1, 0, 0]])

print LA.matrix_power(a, 9)
