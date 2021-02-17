import numpy as np

A = np.array([
    [3, 1],
    [5, 7]
])

B = np.array([
    4,
    2
])

print(np.matmul(A, B))
print(np.matmul(B, A))