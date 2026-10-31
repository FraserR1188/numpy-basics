import numpy as np

a_1d = np.array([-1, 0, 1])

bool_idx = np.array([True, False, True])

print(a_1d[bool_idx])  # Accessing elements using boolean indexing

print(a_1d[a_1d > 0])  # Accessing elements greater than 0

first_ten = np.arange(10)
even_numbers = (first_ten % 2 == 0)
print(first_ten[even_numbers])  # Accessing even numbers using boolean indexing

a_2d = np.array([
    [-1, 0, 1],
    [-2, -1, 0],
    [-3, -2, -1]
])

print(a_2d[a_2d < -1])
