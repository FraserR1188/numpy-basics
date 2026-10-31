import numpy as np

a_1d = np.array([1,2,3,4,5,6])

a_2d = a_1d.reshape((2, 3))
print(a_2d)


a_3d = a_1d.reshape((2, 1, 3))
print(a_3d)

# flattening process

flattened = a_2d.reshape(-1)
print(flattened)

flattened[5] = 42
print(a_2d)  # The original array is modified because flattened is a view of a_2d