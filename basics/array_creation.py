# ----------------------------------
# NumPy Array Creation
# ----------------------------------
# This file covers different ways to create NumPy arrays.

import numpy as np

# -----------------------------
# Creating array from list
# -----------------------------
arr1 = np.array([1, 2, 3, 4, 5])
print("Array from list:", arr1)

# -----------------------------
# Creating 2D array
# -----------------------------
arr2 = np.array([[1, 2, 3],
                 [4, 5, 6]])
print("2D array:\n", arr2)

# -----------------------------
# Using arange()
# -----------------------------
# Similar to Python range()
arr3 = np.arange(0, 10, 2)
print("Array using arange():", arr3)

# -----------------------------
# Using linspace()
# -----------------------------
# Creates evenly spaced values
arr4 = np.linspace(1, 10, 5)
print("Array using linspace():", arr4)

# -----------------------------
# Creating arrays with zeros and ones
# -----------------------------
zeros_arr = np.zeros(5)
ones_arr = np.ones(5)

print("Zeros array:", zeros_arr)
print("Ones array:", ones_arr)

# -----------------------------
# Creating identity matrix
# -----------------------------
identity = np.eye(3)
print("Identity matrix:\n", identity)

# -----------------------------
# Practice examples
# -----------------------------

# Create array of first 10 natural numbers
practice1 = np.arange(1, 11)
print("First 10 natural numbers:", practice1)

# Create 3x3 matrix of zeros
practice2 = np.zeros((3, 3))
print("3x3 zeros matrix:\n", practice2)
