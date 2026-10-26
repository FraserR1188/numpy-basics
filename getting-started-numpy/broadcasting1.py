import numpy as np

a = np.array([1,2,3])
b = 2
result = a + b
print(result)  # Output: [3 4 5]
print(f"A shape: {0}", np.shape(a))  # Output: (3,)
print(f"B shape: {0}", np.shape(b))  # Output: ()

a = np.array([[1, 2, 3], [4, 5, 6]])
b = np.array([0,5,10])

# error
result = a + b
print(result)  # Output: [[ 1  7 13] [ 4 10 16]]
