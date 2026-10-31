import numpy as np

a_1d = np.array([9, 6, 4, 8, 3, 1])
print(a_1d[1:4:1]) # Slicing from index 1 to 4 with a step of 1
print(a_1d[1:4])

print(a_1d[5:1:-1]) # Slicing from index 5 to 1 with a step of -1

print(a_1d[2:-2]) # Slicing from index 2 to the second-to-last element

a_2d = np.array([[1, 2, 3], 
                 [4, 5, 6], 
                 [7, 8, 9]])
print(a_2d[1:3, 0:2]) # Slicing rows 1 to 3 and columns 0 to 2