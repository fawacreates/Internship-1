# Week 1 Practice: NumPy Fundamentals
# NumPy is critical for CV, ML, and aerospace calculations

import numpy as np

print("=== NumPy Basics for Aerospace ===")

"""
Part 1: Array Creation and Manipulation
"""

# Create arrays
array_1d = np.array([1, 2, 3, 4, 5])
array_2d = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

print(f"\n1D Array: {array_1d}")
print(f"2D Array:\n{array_2d}")
print(f"Shape: {array_2d.shape}")
print(f"Data type: {array_2d.dtype}")

# Special arrays
zeros = np.zeros((3, 3))
ones = np.ones((2, 4))
identity = np.eye(3)  # Identity matrix
range_arr = np.arange(0, 10, 2)  # Start, stop, step
linspace = np.linspace(0, 10, 5)  # Start, stop, num_points

print(f"\nIdentity Matrix:\n{identity}")
print(f"Range (0 to 10, step 2): {range_arr}")
print(f"Linspace (0 to 10, 5 points): {linspace}")

"""
Part 2: Vector Operations (Critical for Aerospace)
"""

print("\n--- Vector Operations ---")

# Define position vectors (in aerospace, often in 3D)
position_1 = np.array([10.0, 20.0, 30.0])  # x, y, z (meters)
position_2 = np.array([15.0, 25.0, 35.0])

# Element-wise operations
print(f"Position 1: {position_1}")
print(f"Position 2: {position_2}")
print(f"Difference: {position_2 - position_1}")

# Magnitude (norm) of a vector
magnitude = np.linalg.norm(position_1)
print(f"Magnitude of position 1: {magnitude:.2f} m")

# Dot product (useful for angles)
vel_1 = np.array([1.0, 0.0, 0.0])
vel_2 = np.array([0.707, 0.707, 0.0])  # 45° rotation

dot_product = np.dot(vel_1, vel_2)
print(f"\nDot product (vel1 · vel2): {dot_product:.3f}")

# Cross product (useful for orientation, torque calculations)
z_axis = np.array([0, 0, 1])
y_axis = np.array([0, 1, 0])

cross = np.cross(z_axis, y_axis)
print(f"Z × Y: {cross} (gives X-axis)")

"""
Part 3: Matrix Operations
"""

print("\n--- Matrix Operations ---")

# Create matrices
A = np.array([
    [1, 2],
    [3, 4]
])

B = np.array([
    [5, 6],
    [7, 8]
])

print(f"Matrix A:\n{A}")
print(f"Matrix B:\n{B}")

# Matrix multiplication
C = np.dot(A, B)
print(f"\nA · B (matrix multiply):\n{C}")

# Transpose
A_T = A.T
print(f"\nA^T (transpose):\n{A_T}")

# Inverse (important for coordinate transformations)
A_inv = np.linalg.inv(A)
print(f"\nA^-1 (inverse):\n{A_inv}")

# Verify A * A^-1 = I
I = np.dot(A, A_inv)
print(f"A · A^-1 (should be identity):\n{np.round(I, decimals=10)}")

"""
Part 4: Broadcasting (Vectorization)
"""

print("\n--- Broadcasting ---")

# Broadcasting: operations on arrays of different shapes
scalar = 2
vector = np.array([1, 2, 3])
matrix = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

print(f"Vector: {vector}")
print(f"Vector * 2: {vector * scalar}")
print(f"\nMatrix:\n{matrix}")
print(f"Matrix / 2:\n{matrix / scalar}")

"""
Part 5: Aerospace Application - Coordinate Transformation
"""

print("\n--- Aerospace Example: Rotation Matrix ---")

# Rotation matrix around Z-axis by 45 degrees
theta = np.radians(45)  # Convert to radians
R_z = np.array([
    [np.cos(theta), -np.sin(theta), 0],
    [np.sin(theta), np.cos(theta), 0],
    [0, 0, 1]
])

print(f"Rotation matrix (45° around Z):\n{R_z}")

# Apply rotation to a point
point = np.array([1, 0, 0])
rotated_point = np.dot(R_z, point)

print(f"\nOriginal point: {point}")
print(f"After 45° rotation: {np.round(rotated_point, decimals=3)}")

"""
Part 6: Statistical Operations
"""

print("\n--- Statistics (IMU/Sensor Data) ---")

# Simulated sensor data (e.g., accelerometer readings)
accel_data = np.array([
    [9.8, 0.1, 0.05],
    [9.85, 0.12, 0.04],
    [9.75, 0.08, 0.06],
    [9.88, 0.11, 0.05],
    [9.82, 0.09, 0.07]
])

print("Accelerometer data (5 samples, x/y/z):")
print(accel_data)

mean = np.mean(accel_data, axis=0)
std = np.std(accel_data, axis=0)
min_val = np.min(accel_data, axis=0)
max_val = np.max(accel_data, axis=0)

print(f"\nMean: {mean}")
print(f"Std Dev: {std}")
print(f"Min: {min_val}")
print(f"Max: {max_val}")
