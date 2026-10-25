import numpy as np
import matplotlib.pyplot as plt

x = np.array([-2, -1, 0, 1, 2])

mask = x > 0

print(x[mask])

print(x[x > 0])

mask = x % 2 == 0

print(x[mask])