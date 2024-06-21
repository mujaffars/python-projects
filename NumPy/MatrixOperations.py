import numpy as np

# Create two 2x2 matrices
matrix_a = np.array([[1, 2], [3, 4]])
matrix_b = np.array([[5, 6], [7, 8]])

# Perform matrix multiplication
matrix_product = np.dot(matrix_a, matrix_b)
print("Matrix Product (A * B):")
print(matrix_product)

# Compute the transpose of matrix_a
transpose_a = np.transpose(matrix_a)
print("\nTranspose of Matrix A:")
print(transpose_a)

# Compute the determinant of matrix_a
determinant_a = np.linalg.det(matrix_a)
print("\nDeterminant of Matrix A:")
print(determinant_a)
