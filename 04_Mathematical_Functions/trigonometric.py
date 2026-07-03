# ----------------------------------
# NumPy Trigonometric Functions
# ----------------------------------
# NumPy provides vectorized trigonometric functions
# that work element-wise on arrays.

import numpy as np

# -----------------------------
# Angles in degrees
# -----------------------------
angles_deg = np.array([0, 30, 45, 60, 90])
print("Angles (degrees):", angles_deg)

# -----------------------------
# Convert degrees to radians
# -----------------------------
angles_rad = np.deg2rad(angles_deg)
print("Angles (radians):", angles_rad)

# -----------------------------
# Trigonometric functions
# -----------------------------
print("Sine values:", np.sin(angles_rad))
print("Cosine values:", np.cos(angles_rad))
print("Tangent values:", np.tan(angles_rad))

# -----------------------------
# Inverse trigonometric functions
# -----------------------------
values = np.array([0.0, 0.5, 1.0])

print("arcsin (radians):", np.arcsin(values))
print("arccos (radians):", np.arccos(values))
print("arctan (radians):", np.arctan(values))

# -----------------------------
# Convert radians to degrees
# -----------------------------
print("arcsin (degrees):", np.rad2deg(np.arcsin(values)))

# -----------------------------
# Practice examples
# -----------------------------

# 1. sin values for angles 0 to 180 (step 45)
angles = np.arange(0, 181, 45)
radians = np.deg2rad(angles)
print("Angles:", angles)
print("sin values:", np.sin(radians))

# 2. Verify trigonometric identity
# sin^2(theta) + cos^2(theta) = 1
theta = np.deg2rad(60)
identity = np.sin(theta)**2 + np.cos(theta)**2
print("sin^2 + cos^2:", identity)
