# ----------------------------------
# NumPy Beginner Practice Problems
# ----------------------------------
# This file contains beginner-level practice problems
# to strengthen NumPy fundamentals.

import numpy as np

# -----------------------------
# 1. Create a NumPy array from a list
# -----------------------------
arr = np.array([10, 20, 30, 40, 50])
print("Array:", arr)

# -----------------------------
# 2. Create an array of zeros and ones
# -----------------------------
zeros = np.zeros(5)
ones = np.ones(5)
print("Zeros:", zeros)
print("Ones:", ones)

# -----------------------------
# 3. Create an array using arange
# -----------------------------
range_arr = np.arange(1, 11)
print("Range array:", range_arr)

# -----------------------------
# 4. Find shape, size, and dtype
# -----------------------------
print("Shape:", arr.shape)
print("Size:", arr.size)
print("Data type:", arr.dtype)

# -----------------------------
# 5. Indexing and slicing
# -----------------------------
print("First element:", arr[0])
print("Last three elements:", arr[-3:])

# -----------------------------
# 6. Arithmetic operations
# -----------------------------
print("Add 5:", arr + 5)
print("Multiply by 2:", arr * 2)

# -----------------------------
# 7. Find sum and mean
# -----------------------------
print("Sum:", np.sum(arr))
print("Mean:", np.mean(arr))

# -----------------------------
# 8. Reshape an array
# -----------------------------
reshaped = np.arange(1, 7).reshape(2, 3)
print("Reshaped array:\n", reshaped)

# -----------------------------
# 9. Stack arrays vertically
# -----------------------------
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
v_stack = np.vstack((a, b))
print("Vertical stack:\n", v_stack)

# -----------------------------
# 10. Apply condition on array
# -----------------------------
greater_than_25 = arr[arr > 25]
print("Elements greater than 25:", greater_than_25)
