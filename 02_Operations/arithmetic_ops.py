# ----------------------------------
# NumPy Arithmetic Operations
# ----------------------------------
# NumPy allows element-wise arithmetic operations on arrays.

import numpy as np

# Creating arrays
a = np.array([10, 20, 30, 40])
b = np.array([1, 2, 3, 4])

print("Array a:", a)
print("Array b:", b)

# -----------------------------
# Addition
# -----------------------------
print("Addition:", a + b)

# -----------------------------
# Subtraction
# -----------------------------
print("Subtraction:", a - b)

# -----------------------------
# Multiplication
# -----------------------------
print("Multiplication:", a * b)

# -----------------------------
# Division
# -----------------------------
print("Division:", a / b)

# -----------------------------
# Power
# -----------------------------
print("Power (a^2):", a ** 2)

# -----------------------------
# Operations with scalar
# -----------------------------
print("Add scalar:", a + 5)
print("Multiply scalar:", a * 2)

# -----------------------------
# Arithmetic using NumPy functions
# -----------------------------
print("np.add:", np.add(a, b))
print("np.subtract:", np.subtract(a, b))
print("np.multiply:", np.multiply(a, b))
print("np.divide:", np.divide(a, b))

# -----------------------------
# Practice examples
# -----------------------------

# 1. Increase all elements by 10
increased = a + 10
print("Increased by 10:", increased)

# 2. Find square of all elements
squared = a * a
print("Squared elements:", squared)
