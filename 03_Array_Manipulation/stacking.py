# ----------------------------------
# NumPy Array Stacking
# ----------------------------------
# Stacking is used to combine multiple arrays
# along different axes.

import numpy as np

# Creating sample arrays
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

print("Array a:", a)
print("Array b:", b)

# -----------------------------
# Vertical stacking (vstack)
# -----------------------------
v_stack = np.vstack((a, b))
print("Vertical Stack:\n", v_stack)

# -----------------------------
# Horizontal stacking (hstack)
# -----------------------------
h_stack = np.hstack((a, b))
print("Horizontal Stack:", h_stack)

# -----------------------------
# Using stack()
# -----------------------------
# axis = 0 → row-wise
# axis = 1 → column-wise

stack_axis0 = np.stack((a, b), axis=0)
stack_axis1 = np.stack((a, b), axis=1)

print("Stack axis=0:\n", stack_axis0)
print("Stack axis=1:\n", stack_axis1)

# -----------------------------
# Stacking 2D arrays
# -----------------------------
arr1 = np.array([[1, 2],
                 [3, 4]])

arr2 = np.array([[5, 6],
                 [7, 8]])

print("2D vstack:\n", np.vstack((arr1, arr2)))
print("2D hstack:\n", np.hstack((arr1, arr2)))

# -----------------------------
# Practice examples
# -----------------------------

# 1. Stack three arrays vertically
x = np.array([10, 20, 30])
y = np.array([40, 50, 60])
z = np.array([70, 80, 90])

combined = np.vstack((x, y, z))
print("Combined stack:\n", combined)
