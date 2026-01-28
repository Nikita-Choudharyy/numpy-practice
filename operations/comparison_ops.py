# ----------------------------------
# NumPy Comparison Operations
# ----------------------------------
# Comparison operations return boolean arrays
# and are commonly used in filtering and conditions.

import numpy as np

# Creating arrays
a = np.array([10, 20, 30, 40])
b = np.array([15, 20, 25, 40])

print("Array a:", a)
print("Array b:", b)

# -----------------------------
# Element-wise comparisons
# -----------------------------
print("a == b:", a == b)
print("a != b:", a != b)
print("a > b:", a > b)
print("a < b:", a < b)
print("a >= b:", a >= b)
print("a <= b:", a <= b)

# -----------------------------
# Comparisons with scalar
# -----------------------------
print("a > 25:", a > 25)
print("a <= 20:", a <= 20)

# -----------------------------
# Using comparison results
# -----------------------------
# Filtering values based on condition
greater_than_20 = a[a > 20]
print("Elements greater than 20:", greater_than_20)

# -----------------------------
# Using NumPy comparison functions
# -----------------------------
print("np.equal:", np.equal(a, b))
print("np.greater:", np.greater(a, b))
print("np.less_equal:", np.less_equal(a, b))

# -----------------------------
# Practice examples
# -----------------------------

# 1. Find elements less than 30
less_than_30 = a[a < 30]
print("Elements less than 30:", less_than_30)

# 2. Check which elements are equal in a and b
equal_elements = a[a == b]
print("Equal elements:", equal_elements)
