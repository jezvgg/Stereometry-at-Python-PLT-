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
edge_n = 18
z_n = 15
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
    return math.sqrt((point2[0]-point1[0])**2 + (point2[1]-point1[1])**2 + (point2[2]-point1[2])**2)


x = np.array([])
y = np.array([])
z = np.array([])

center_0 = sum(points[:, 0]) / len(points)
center_1 = sum(points[:, 1]) / len(points)

for Z in sorted(list(set(points[: ,2])))[:-1]:
    center_0 = sum(points[:, 0]) / len(points)
    center_1 = sum(points[:, 1]) / len(points)
    slide = sorted(points[points[:, 2]==Z], key=lambda point: math.atan2(point[1]-center_1, point[0]-center_0))
    for point in slide:
        point1 = min(points[points[:, 2] > Z], key = lambda x: distance(point, x))
        x = np.append(x, [point[0], point1[0], point[0]])
        y = np.append(y, [point[1], point1[1], point[1]])
        z = np.append(z, [point[2], point1[2], point[2]])
    point = slide[0]
    x = np.append(x, [point[0]])
    y = np.append(y, [point[1]])
    z = np.append(z, [point[2]])

slide = np.array(sorted(points[points[:, 2] == sorted(list(set(points[: ,2])))[-1]], key=lambda point: math.atan2(point[1]-center_1, point[0]-center_0)))
x = np.append(x, slide[:, 0])
y = np.append(y, slide[:, 1])
z = np.append(z, slide[:, 2])
x = np.append(x, slide[0, 0])
y = np.append(y, slide[0, 1])
z = np.append(z, slide[0, 2])
    
ax.plot(x, y, z, 'b')

ax.set_xlim([points.min(), points.max()])
ax.set_ylim([points.min(), points.max()])
ax.set_zlim([points.min(), points.max()])
plt.show()