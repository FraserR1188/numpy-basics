import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(0, 10, 100)
x = np.cos(t)
y = np.sin(t)
z = t / 2

traj = np.zeros((100, 3), dtype=np.float64)
traj[:, 0] = x
traj[:, 1] = y
traj[:, 2] = z

print("Trajectory shape:", traj.shape)
print("Time shape:", t.shape)
print("Trajectory size:", traj.size)
print("Time size:", t.size)
print("Trajectory dimensions:", traj.ndim)
print("Time dimensions:", t.ndim)
print("Trajectory data type:", traj.dtype)
print("Time data type:", t.dtype)

fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111, projection='3d')
ax.plot(x,y,z, 'b-', label='Trajectory')
ax.set_xlabel('km')
ax.set_ylabel('km')
ax.set_zlabel('km')

plt.show()