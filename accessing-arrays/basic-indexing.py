import numpy as np

a_1d = np.array([9, 6, 4])
print(a_1d[0])  # Accessing the first element
print(a_1d[1])  # Accessing the second element
print(a_1d[2])  # Accessing the third element
print(a_1d[-1]) # Accessing the last element
print(a_1d[-2]) # Accessing the second-to-last element
print(a_1d[-3]) # Accessing the third-to-last element

a_2d = np.array([
    [11, 12, 13],
    [21, 22, 23],
    [31, 32, 33]
])

print(a_2d[0, 0])  # Accessing the first row, first column
print(a_2d[0, 1])  # Accessing the first row, second column

second_row = a_2d[1]  # Accessing the second row
print(second_row)

second_row[0] = 210
print(a_2d)
