import numpy as np

# Generating one-dimensional (1D) array
a = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
print(a)

# Generating one-dimensional (2D) array
b = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# Checking the shape (dimension) and size of the array
print(a.shape)  # (10,)
print(b.shape)  # (3,3)

print(a.size)  # 10
print(b.size)  # 9

# Check the type
print(type(a))  # numpy.ndarray
print(type(b))  # numpy.ndarray

print(a.dtype)  # dtype('int64')
print(b.dtype)  # dtype('int64')

# Maximum and Minimum values
print(np.max(a))  # 9
print(np.min(a))  # 0

# Index of maximum and minimum values
a = np.array([4, 2, 3, 13, 5, 7, 14])
print(max(a))  # 14
print(a.max())  # 14
print(min(a))  # 2
print(a.min())  # 2

# Index of max and min values
print(a.argmax())  # 6
print(a.argmin())  # 1
