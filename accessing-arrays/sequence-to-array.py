import numpy as np

ints = [-2, -1, 0, 1, 2]

int_array = np.array(ints)

print(int_array)

matrix = np.array([[1, 2, 3], [4, 5, 6]])

print(matrix)

array_3d = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])

print(array_3d)

ints = np.array(ints, dtype=np.short)
print(ints.dtype)