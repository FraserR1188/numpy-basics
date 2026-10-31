import numpy as np

a_2x3 = np.array([[1, 2, 3], [4, 5, 6]])

for row in a_2x3:
    print(row)  # Each row is printed as a 1D array

for row in a_2x3:
    for element in row:
        print(element)  # Each element is printed individually

a_3x2x3 = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]], [[13, 14, 15], [16, 17, 18]]])

#Iterating using Python for loop

for depth in a_3x2x3:
    for row in depth:
        for element in row:
            print(element)  # Each element is printed individually


for element in np.nditer(a_3x2x3):
    print(element)  # Each element is printed individually using nditer


a_2x3 = np.arange(6).reshape((2, 3))
print("Original array:\n", a_2x3)

print("Default ordeer:")
for element in np.nditer(a_2x3):
    print(element)  # Iterating in default order

print("Fortran order:")
for element in np.nditer(a_2x3, order='F'):
    print(element)  # Iterating in Fortran order - column first order

for element in np.nditer(a_2x3, op_flags=['readwrite']):
    element[...] = 0

print("Modified array:\n", a_2x3)  # The original array is modified because nditer returns a view of the array
