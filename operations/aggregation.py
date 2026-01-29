# ----------------------------------
# NumPy Aggregation Operations
# ----------------------------------
# Aggregation functions are used to summarize data
# such as sum, mean, min, max, etc.

import numpy as np

# Creating arrays
arr1 = np.array([10, 20, 30, 40, 50])
arr2 = np.array([[1, 2, 3],
                 [4, 5, 6]])

print("1D Array:", arr1)
print("2D Array:\n", arr2)

# -----------------------------
# Basic aggregation functions
# -----------------------------
print("Sum:", np.sum(arr1))
print("Mean:", np.mean(arr1))
print("Minimum:", np.min(arr1))
print("Maximum:", np.max(arr1))

# -----------------------------
# Other useful aggregations
# -----------------------------
print("Standard Deviation:", np.std(arr1))
print("Variance:", np.var(arr1))

# -----------------------------
# Aggregation with axis
# -----------------------------
# axis = 0 → column-wise
# axis = 1 → row-wise

print("Column-wise sum:", np.sum(arr2, axis=0))
print("Row-wise sum:", np.sum(arr2, axis=1))

print("Column-wise mean:", np.mean(arr2, axis=0))
print("Row-wise mean:", np.mean(arr2, axis=1))

# -----------------------------
# Using aggregation methods
# -----------------------------
print("arr1.sum():", arr1.sum())
print("arr1.mean():", arr1.mean())
print("arr1.max():", arr1.max())

# -----------------------------
# Practice examples
# -----------------------------

# 1. Find average of elements greater than 25
avg_gt_25 = np.mean(arr1[arr1 > 25])
print("Average of elements > 25:", avg_gt_25)

# 2. Find max value in each row
row_max = np.max(arr2, axis=1)
print("Maximum in each row:", row_max)
