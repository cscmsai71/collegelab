import numpy as np
m=np.array([[1,2,3],
            [4,5,6],
            [7,8,9]])
print("printing the original square array:\n",m)
m,v=np.linalg.eig(m)
print("printing the eigen values of the given square array:\n",m)
print("printing right eigen values of the given square array:\n",v)