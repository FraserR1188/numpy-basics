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

z_threshold = 3.0
mask = traj[:, 2] > z_threshold
low_altitude_points = traj[mask, :]

fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111, projection='3d')
ax.plot(x,y,z, 'b-', label='Trajectory')
ax.scatter(low_altitude_points[:, 0], low_altitude_points[:, 1], low_altitude_points[:, 2], c='r', label='Low Altitude Points')
ax.set_xlabel('km')
ax.set_ylabel('km')
ax.set_zlabel('km')

plt.show()