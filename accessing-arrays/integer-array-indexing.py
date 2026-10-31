import numpy as np

a_2d = np.array([
    [11, 12, 1, 14],
    [21, 22, 23, 24],
    [31, 32, 33, 34]
])

print(a_2d[1, 2]) # Accessing the element in the second row, third column
print(a_2d[[1, 2]]) # Accessing the second and third rows

print(a_2d[[1, 2], 1]) # Accessing the second column of the second and third rows
print(a_2d[[0, 2], [1, 3]]) # Accessing elements at (1,1) and (2,2)

"""
Note that advanced indexing returns a copy of the data unlike basic indexing, which returns a view instead. Thus, if you modify the data returned from advanced indexing, the original array won't be affected.
"""
