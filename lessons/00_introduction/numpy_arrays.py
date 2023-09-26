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

# Range

c = np.arange(0, 10)
print(c)  # [0,1,2,3,4,5,6,7,8,9]

d = np.arange(0, 11, 2)
print(d)  # [0,2,4,6,8,10]

# Linspace

x1 = np.linspace(0, 20, 5)  # 3rd arg is the count of the numbers to generate
print(x1)  # [0., 7., 10.,15.,20.]

x2 = np.linspace(0, 10, 3)
print(x2)  # [0., 5., 10.]

x3 = np.linspace(0, 10, 50)  # Will generate 50 numbers between 0 and 10
print(x3)
print(x3.shape)  # (50,)

# Reshape
y = np.arange(0, 25)
print(y)  # [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24]
print(y.shape)  # (25,)
print(y.reshape(5, 5))  # [[0,1,2,3,4],[5,6,7,8,9],[10,11,12,13,14],[15,16,17,18,19],[20,21,22,23,24]]
print(y.reshape(1, 25))  # [[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24]]
print(y.reshape(25,
                1))  # [[0],[1],[2],[3],[4],[5],[6],[7],[8],[9],[10],[11],[12],[13],[14],[15],[16],[17],[18],[19],[20],[21],[22],[23],[24]]]

# Zeroes and ones

print(np.zeros(3))  # [0.,0.,0.]
print(np.zeros(shape=(3, 3)))  # [[0.,0.,0.],[0.,0.,0.],[0.,0.,0.]]
print(np.zeros((3, 3)))  # [[0.,0.,0.],[0.,0.,0.],[0.,0.,0.]]

print(np.ones(5))  # [1.,1.,1.,1.,1.]
print(np.ones((4, 3)))  # [[1.,1.,1.],[1.,1.,1.],[1.,1.,1.],[1.,1.,1.]]
print(7 * np.ones((3, 3)))  # [[7.,7.,7.],[7.,7.,7.],[7.,7.,7.],[7.,7.,7.]]

# Eye, generating Identity Matrix
print(np.eye(3))  # [[1.,0.,0.],[0.,1.,0.],[0.,0.,1.]]

# Random Numbers: rand, randint
x1 = np.random.randn(3, 3)  # will generate random numbers from normal distribution
print(x1)

x2 = np.random.rand(3, 3)  # will generate random numbers between 0 and 1
print(x2)

x3 = np.random.randint(3, 8, 10)  # will generate 10 random integers between 3 and 8
print(x3)

# Indexing and slicing with 1D Array
ar = np.array([4, 2, 3, 13, 5, 7, 14])
print(ar)  # [4, 2, 3, 13, 5, 7, 14]
print(ar[3])  # 13
print(ar[1:4])  # [2,3,13]
print(ar[-1])  # extracting last member of array: 14
print(ar[1:])  # Slicing from index 1 to end
print(ar[:4])  # Slicing upto index 3
print(ar[:-1])  # Include everything except the last member of array
print(ar[::-1])  # Reversing or flipping the array

# Indexing of sub-array and sub-matrix from 2D (matrix) array
arr = np.arange(1, 17).reshape(4, 4)
print(arr)  # [[1,2,3,4],[5,6,7,8],[9,10,11,12], [13,14,15,16]]
print(arr[0])  # [1,2,3,4]
print(arr[3])  # [13,14,15,16]
print(arr[2][1])  # 10
print(arr[2, 1])  # 10
print(arr[1:3, 1:3])  # [[6,7],[10,11]]
print(arr[:, 3])  # Extracting last column [4,8,12,16]
print(arr[:, 3].reshape(-1, 1))  # Extracting last column vertically: [[4],[8],[12],[16]]
print(arr[:, 3:])  # Other way of Extracting last column vertically:[[4],[8],[12],[16]]
