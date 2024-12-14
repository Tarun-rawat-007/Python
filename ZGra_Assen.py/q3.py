import numpy as np


matrix = np.random.randint(1, 101, size=(4, 4))
print("Original Matrix:\n", matrix)


matrix_min = matrix.min()
matrix_max = matrix.max()
normalized_matrix = (matrix - matrix_min) / (matrix_max - matrix_min)

print("\nNormalized Matrix:\n", normalized_matrix)
