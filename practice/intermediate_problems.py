# ----------------------------------
# NumPy Intermediate Practice Problems
# ----------------------------------
# This file contains intermediate-level problems
# to strengthen NumPy concepts used in data analysis.

import numpy as np

# -----------------------------
# 1. Boolean masking
# -----------------------------
arr = np.array([12, 5, 30, 18, 45, 7, 22])
filtered = arr[arr > 20]
print("Elements greater than 20:", filtered)

# -----------------------------
# 2. Replace values using condition
# -----------------------------
replaced = np.where(arr >= 20, "high", "low")
print("High/Low labels:", replaced)

# -----------------------------
# 3. Axis-based aggregation
# -----------------------------
matrix = np.array([[10, 20, 30],
                   [40, 50, 60]])

print("Column-wise sum:", np.sum(matrix, axis=0))
print("Row-wise mean:", np.mean(matrix, axis=1))

# -----------------------------
# 4. Reshape and flatten
# -----------------------------
reshaped = np.arange(1, 13).reshape(3, 4)
print("Reshaped (3x4):\n", reshaped)

flattened = reshaped.flatten()
print("Flattened array:", flattened)

# -----------------------------
# 5. Stacking arrays
# -----------------------------
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

v_stack = np.vstack((a, b))
h_stack = np.hstack((a, b))

print("Vertical stack:\n", v_stack)
print("Horizontal stack:", h_stack)

# -----------------------------
# 6. Splitting arrays
# -----------------------------
split_arr = np.split(np.array([10, 20, 30, 40, 50, 60]), 3)
print("Split array:", split_arr)

# -----------------------------
# 7. Universal functions
# -----------------------------
values = np.array([1, 4, 9, 16])
print("Square root:", np.sqrt(values))
print("Exponential:", np.exp(values))

# -----------------------------
# 8. Trigonometric functions
# -----------------------------
angles = np.array([0, 30, 60, 90])
radians = np.deg2rad(angles)
print("Sine values:", np.sin(radians))

# -----------------------------
# 9. Dot product
# -----------------------------
x = np.array([2, 3, 4])
y = np.array([1, 5, 7])

dot = np.dot(x, y)
print("Dot product:", dot)

# -----------------------------
# 10. Matrix operations
# -----------------------------
A = np.array([[1, 2],
              [3, 4]])

B = np.array([[2, 0],
              [1, 2]])

product = A @ B
print("Matrix multiplication:\n", product)
