import numpy as np
from numpy.linalg import norm
A=np.array([2,1,2,3,2,9])
B=np.array([3,4,2,4,5,5])
print("A:",A)
print("B:",B)
cosine=np.dot(A,B)/(norm(A)*norm(B))
print("cosine similarity:",cosine)