import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import math

fig = plt.figure()
ax = plt.subplot(111, projection='3d')

# x y z

r = 1
h = 1
c_x = 1
c_y =2
c_z = 3

# цилиндр
edge_n = 13
z_n = 16
edge = np.linspace(0, 2*np.pi, edge_n)
x = np.array([])
y = np.array([])
z = np.array([])
for Z in np.linspace(0, np.pi, z_n):
    x = np.append(x,np.sin(edge)*np.sin(Z))
    y = np.append(y,np.cos(edge)*np.sin(Z))
    z = np.append(z,[np.cos(Z)]*edge_n)

points = np.array(list(zip(x,y,z)))

# points = np.array([
#     [0, 0, 2],
#     [0, 1, 0],
#     [0, 0, 0],
#     [0, 1, 2],
#     [1, 0, 0],
#     [1, 0, 2],
#     [1, 1, 0],
#     [1, 1, 2]
# ])


def distance(point1: list, point2: list):
    return ((point2[0]-point1[0])**2 + (point2[1]-point1[1])**2 + (point2[2]-point1[2])**2)**0.5

neightbors = 5
x = np.array([])
y = np.array([])
z = np.array([])
for point in points:
    for point2 in sorted(points, key=lambda x: distance(x, point))[:neightbors]:
        x = np.append(x, np.array([point[0], point2[0]]))
        y = np.append(y, np.array([point[1], point2[1]]))
        z = np.append(z, np.array([point[2], point2[2]]))
ax.plot(x, y, z, 'b')

ax.set_xlim([points.min(), points.max()])
ax.set_ylim([points.min(), points.max()])
ax.set_zlim([points.min(), points.max()])
plt.show()