# ----------------------------------
# NumPy Array Attributes
# ----------------------------------
# This file explains important attributes of NumPy arrays:
# ndim, shape, size, and dtype.

import numpy as np

# Creating sample arrays
arr1 = np.array([1, 2, 3, 4, 5])
arr2 = np.array([[1, 2, 3],
                 [4, 5, 6]])

print("1D array:", arr1)
print("2D array:\n", arr2)

# -----------------------------
# ndim (number of dimensions)
# -----------------------------
print("arr1 ndim:", arr1.ndim)
print("arr2 ndim:", arr2.ndim)

# -----------------------------
# shape (dimensions of array)
# -----------------------------
print("arr1 shape:", arr1.shape)
print("arr2 shape:", arr2.shape)

# -----------------------------
# size (total number of elements)
# -----------------------------
print("arr1 size:", arr1.size)
print("arr2 size:", arr2.size)

# -----------------------------
# dtype (data type of elements)
# -----------------------------
print("arr1 dtype:", arr1.dtype)
print("arr2 dtype:", arr2.dtype)

# -----------------------------
# Practice examples
# -----------------------------

# Float array
float_arr = np.array([1.5, 2.3, 4.8])
print("Float array:", float_arr)
print("Float array dtype:", float_arr.dtype)

# Mixed type array
mixed_arr = np.array([1, 2.5, 3])
print("Mixed array:", mixed_arr)
print("Mixed array dtype:", mixed_arr.dtype)
