# ----------------------------------
# NumPy Array Reshaping
# ----------------------------------
# Reshaping changes the shape of an array
# without changing its data.

import numpy as np

# -----------------------------
# Creating a 1D array
# -----------------------------
arr = np.array([1, 2, 3, 4, 5, 6])
print("Original array:", arr)
print("Original shape:", arr.shape)

# -----------------------------
# Reshape 1D to 2D
# -----------------------------
reshaped = arr.reshape(2, 3)
print("Reshaped array (2x3):\n", reshaped)
print("Reshaped shape:", reshaped.shape)

# -----------------------------
# Reshape using -1
# -----------------------------
# NumPy automatically calculates the missing dimension
auto_reshape = arr.reshape(-1, 2)
print("Auto reshaped (-1,2):\n", auto_reshape)

# -----------------------------
# Flattening an array
# -----------------------------
flattened = reshaped.flatten()
print("Flattened array:", flattened)

# -----------------------------
# Ravel (similar to flatten but returns view if possible)
# -----------------------------
raveled = reshaped.ravel()
print("Raveled array:", raveled)

# -----------------------------
# Practice examples
# -----------------------------

# 1. Convert 1D array of 12 elements into 3x4 matrix
arr2 = np.arange(1, 13)
matrix = arr2.reshape(3, 4)
print("3x4 Matrix:\n", matrix)

# 2. Convert 2D array back to 1D
one_d = matrix.reshape(-1)
print("Converted back to 1D:", one_d)
