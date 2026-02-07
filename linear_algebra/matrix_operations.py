# ----------------------------------
# NumPy Matrix Operations
# ----------------------------------
# Matrix operations are widely used in
# linear algebra, data science, and machine learning.

import numpy as np

# -----------------------------
# Creating matrices
# -----------------------------
A = np.array([[1, 2],
              [3, 4]])

B = np.array([[5, 6],
              [7, 8]])

print("Matrix A:\n", A)
print("Matrix B:\n", B)

# -----------------------------
# Matrix addition
# -----------------------------
add_result = A + B
print("Addition:\n", add_result)

# -----------------------------
# Matrix subtraction
# -----------------------------
sub_result = A - B
print("Subtraction:\n", sub_result)

# -----------------------------
# Matrix multiplication
# -----------------------------
mul_result = np.dot(A, B)
print("Multiplication (dot):\n", mul_result)

# Using @ operator
mul_operator = A @ B
print("Multiplication (@):\n", mul_operator)

# -----------------------------
# Element-wise multiplication
# -----------------------------
elementwise_mul = A * B
print("Element-wise multiplication:\n", elementwise_mul)

# -----------------------------
# Transpose of a matrix
# -----------------------------
transpose_A = A.T
print("Transpose of A:\n", transpose_A)

# -----------------------------
# Determinant of a matrix
# -----------------------------
det_A = np.linalg.det(A)
print("Determinant of A:", det_A)

# -----------------------------
# Inverse of a matrix
# -----------------------------
inv_A = np.linalg.inv(A)
print("Inverse of A:\n", inv_A)

# -----------------------------
# Practice examples
# -----------------------------

# 1. Verify A * A_inverse = Identity matrix
identity = A @ inv_A
print("A * A_inverse:\n", identity)

# 2. Transpose of matrix B
print("Transpose of B:\n", B.T)
