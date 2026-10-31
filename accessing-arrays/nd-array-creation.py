import numpy as np

a5x3_zeros = np.zeros((5, 3), dtype=np.uint)
print(a5x3_zeros)

ax4x3x2_zeros = np.zeros((4, 3, 2))
print(ax4x3x2_zeros)

a2x3_ones = np.ones((2, 3))
print(a2x3_ones)

a5x3_pi = np.full((5, 3), np.pi)
print(a5x3_pi)

ax2x2_rand = np.random.rand(2, 2)
print(ax2x2_rand)