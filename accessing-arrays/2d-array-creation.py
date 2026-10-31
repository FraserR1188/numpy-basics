import numpy as np

identity_matrix = np.eye(3)
print(identity_matrix)

indentity_3x4 = np.eye(3, 4)
print(indentity_3x4)

diagonal_matrix = np.diag([2, 3, 4, 5])
print(diagonal_matrix)

diagonal_2D = np.array([
    [1, 0, 0, 0, 0],
    [0, 2, 0, 0, 0],
    [0, 0, 3, 0, 0],
    [0, 0, 0, 4, 0],
    [0, 0, 0, 0, 5]
])
print(diagonal_2D)

diagonal_from_2D = np.diag(diagonal_2D)
print(diagonal_from_2D)