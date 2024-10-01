import numpy as np

# Define the matrices
A = np.array([[1, 0, 4], [0, 1, -10], [0, 0, 1]])
B = np.array([[-1, 0, 0], [0, 1, 0], [1, 0, 0]])
C = np.array([[0, -1, 0], [1, 0, 0], [0, 0, 1]])
D = np.array([[1, 0, 0], [0, 1, 0], [2, 1, 1]])

# Perform the matrix multiplication
result = A @ B @ C @ D

# Output the result
print(result)
