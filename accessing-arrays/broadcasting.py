# Broadcasting makes it possible to perform operations on arrays with different shapes. When operating on two arrays, NumPy compares their shapes element-wise. It starts with the trailing dimensions and works its way forward. Two dimensions are compatible when:
# 1. they are equal, or
# 2. one of them is 1 
import numpy as np

a_2x3 = np.array([[1, 2, 3], [4, 5, 6]])

a_1x3 = np.array([1, 2, 3])

sum = a_2x3 + a_1x3  # Broadcasting occurs here
print(sum) 

c = 3
prod = a_2x3 * c
print(prod)  # Broadcasting occurs here