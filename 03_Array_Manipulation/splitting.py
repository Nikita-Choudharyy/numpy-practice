# ----------------------------------
# NumPy Array Splitting
# ----------------------------------
# Splitting is used to divide an array into multiple sub-arrays.

import numpy as np

# -----------------------------
# Creating arrays
# -----------------------------
arr1 = np.array([10, 20, 30, 40, 50, 60])
arr2 = np.array([[1, 2, 3, 4],
                 [5, 6, 7, 8]])

print("1D Array:", arr1)
print("2D Array:\n", arr2)

# -----------------------------
# Splitting 1D array
# -----------------------------
split_arr = np.split(arr1, 3)
print("Split 1D array:", split_arr)

# -----------------------------
# Horizontal split (hsplit)
# -----------------------------
h_split = np.hsplit(arr2, 2)
print("Horizontal split:")
for part in h_split:
    print(part)

# -----------------------------
# Vertical split (vsplit)
# -----------------------------
v_split = np.vsplit(arr2, 2)
print("Vertical split:")
for part in v_split:
    print(part)

# -----------------------------
# Splitting with indices
# -----------------------------
index_split = np.split(arr1, [2, 4])
print("Split using indices:", index_split)

# -----------------------------
# Practice examples
# -----------------------------

# 1. Split array into two equal parts
arr3 = np.array([1, 2, 3, 4])
parts = np.split(arr3, 2)
print("Equal split:", parts)

# 2. Split 2D array column-wise into 4 parts
arr4 = np.array([[10, 20, 30, 40]])
col_split = np.hsplit(arr4, 4)
print("Column-wise split:", col_split)
