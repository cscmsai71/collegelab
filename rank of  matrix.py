import numpy as np
matrix=np.array([[1,2,3,23],
                 [4,5,6,25],
                 [7,8,9,28],
                 [10,11,12,41]])
print("rank of matrix:",np.linalg.matrix_rank(matrix))