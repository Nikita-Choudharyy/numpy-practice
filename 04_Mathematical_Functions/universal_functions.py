# ----------------------------------
# NumPy Universal Functions (ufuncs)
# ----------------------------------
# Universal functions operate element-wise on arrays
# and are optimized for performance.

import numpy as np

# Creating array
arr = np.array([1, 4, 9, 16, 25])
print("Array:", arr)

# -----------------------------
# Basic mathematical ufuncs
# -----------------------------
print("Square root:", np.sqrt(arr))
print("Exponential:", np.exp(arr))
print("Log (natural):", np.log(arr))

# -----------------------------
# Absolute and power
# -----------------------------
neg_arr = np.array([-1, -4, 9, -16])
print("Absolute values:", np.abs(neg_arr))
print("Power (arr^2):", np.power(arr, 2))

# -----------------------------
# Rounding functions
# -----------------------------
float_arr = np.array([1.2, 2.5, 3.7, 4.1])
print("Round:", np.round(float_arr))
print("Floor:", np.floor(float_arr))
print("Ceil:", np.ceil(float_arr))

# -----------------------------
# Maximum and minimum
# -----------------------------
a = np.array([10, 20, 30])
b = np.array([15, 18, 35])

print("Element-wise max:", np.maximum(a, b))
print("Element-wise min:", np.minimum(a, b))

# -----------------------------
# Practice examples
# -----------------------------

# 1. Calculate cube root of elements
cube_roots = np.cbrt(arr)
print("Cube roots:", cube_roots)

# 2. Clip values within range
clipped = np.clip(a, 15, 25)
print("Clipped values:", clipped)
