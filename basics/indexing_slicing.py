# ----------------------------------
# NumPy Indexing and Slicing
# ----------------------------------
# Indexing and slicing are used to access
# specific elements or parts of an array.

import numpy as np

# -----------------------------
# Creating arrays
# -----------------------------
arr1 = np.array([10, 20, 30, 40, 50])
arr2 = np.array([[1, 2, 3],
                 [4, 5, 6],
                 [7, 8, 9]])

print("1D Array:", arr1)
print("2D Array:\n", arr2)

# -----------------------------
# Indexing in 1D array
# -----------------------------
print("First element:", arr1[0])
print("Last element:", arr1[-1])

# -----------------------------
# Slicing in 1D array
# -----------------------------
print("Elements from index 1 to 3:", arr1[1:4])
print("Elements till index 3:", arr1[:3])
print("Elements from index 2:", arr1[2:])

# -----------------------------
# Indexing in 2D array
# -----------------------------
print("Element at (0,1):", arr2[0, 1])
print("Element at (2,2):", arr2[2, 2])

# -----------------------------
# Slicing in 2D array
# -----------------------------
print("First row:", arr2[0])
print("First column:", arr2[:, 0])
print("Sub-matrix (first 2 rows, first 2 columns):\n", arr2[:2, :2])

# -----------------------------
# Using slicing with step
# -----------------------------
print("Every second element:", arr1[::2])
print("Reverse array:", arr1[::-1])

# -----------------------------
# Practice examples
# -----------------------------

# 1. Extract middle elements from array
mid = arr1[1:4]
print("Middle elements:", mid)

# 2. Get last row of 2D array
last_row = arr2[-1]
print("Last row:", last_row)
