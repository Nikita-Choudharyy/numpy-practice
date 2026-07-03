# ----------------------------------
# Introduction to NumPy
# ----------------------------------
# NumPy (Numerical Python) is a Python library used for
# numerical and scientific computing.
#
# It provides:
# - Multidimensional array objects
# - Fast mathematical operations
# - Efficient handling of large numerical data
#
# NumPy is widely used in Data Science, Machine Learning,
# and Scientific Computing.

import numpy as np

# -----------------------------
# NumPy Version
# -----------------------------
print("NumPy version:", np.__version__)

# -----------------------------
# Why NumPy?
# -----------------------------
# NumPy is preferred over Python lists because it is:
# - Faster
# - Memory efficient
# - Supports vectorized operations

python_list = [1, 2, 3, 4, 5]
numpy_array = np.array([1, 2, 3, 4, 5])

print("Python list:", python_list)
print("NumPy array:", numpy_array)

# -----------------------------
# Example: Vectorized Operation
# -----------------------------
# Python list operation
list_result = [x * 2 for x in python_list]
print("Result using Python list:", list_result)

# NumPy array operation
array_result = numpy_array * 2
print("Result using NumPy array:", array_result)

# -----------------------------
# Where NumPy is Used
# -----------------------------
print("NumPy is a foundational library for Data Science and Machine Learning.")

