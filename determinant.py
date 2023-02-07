import numpy as np
n_array = np.array([[55, 25, 15],
                    [30, 44, 2],
                    [11, 45, 77]])
print("Matrix is:")
print(n_array)
det = np.linalg.det(n_array)
print("Determinant of given 3X3 square matrix:\n")
print(int(det))