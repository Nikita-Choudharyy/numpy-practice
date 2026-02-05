# ----------------------------------
# NumPy Dot Product
# ----------------------------------
# Dot product is a fundamental operation in linear algebra
# and is widely used in machine learning and data science.

import numpy as np

# -----------------------------
# Dot product of 1D arrays (vectors)
# -----------------------------
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

dot_1d = np.dot(a, b)
print("Dot product (1D):", dot_1d)

# -----------------------------
# Using @ operator (same as dot)
# -----------------------------
dot_operator = a @ b
print("Dot product using @:", dot_operator)

# -----------------------------
# Dot product of 2D arrays (matrices)
# -----------------------------
A = np.array([[1, 2],
              [3, 4]])

B = np.array([[5, 6],
              [7, 8]])

dot_2d = np.dot(A, B)
print("Dot product (2D):\n", dot_2d)

# -----------------------------
# Matrix multiplication using @
# -----------------------------
matrix_mult = A @ B
print("Matrix multiplication using @:\n", matrix_mult)

# -----------------------------
# Dot product with transpose
# -----------------------------
C = np.array([[1, 2, 3]])
D = np.array([[4],
              [5],
              [6]])

dot_transpose = C @ D
print("Dot product with transpose:\n", dot_transpose)

# -----------------------------
# Practice examples
# -----------------------------

# 1. Calculate dot product of two vectors
x = np.array([2, 4, 6])
y = np.array([1, 3, 5])
print("Practice dot product:", np.dot(x, y))

# 2. Multiply identity matrix with another matrix
I = np.eye(2)
result = I @ A
print("Identity matrix multiplication:\n", result)
