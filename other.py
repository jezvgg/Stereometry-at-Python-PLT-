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

edge = np.linspace(0, 2*np.pi, 13)
x = np.array([])
y = np.array([])
z = np.array([])
x = np.append(x,c_x+r*np.sin(edge))
y = np.append(y,c_y+r*np.cos(edge))
z = np.append(z,[c_z]*13)
x = np.append(x,c_x+r*np.sin(edge))
y = np.append(y,c_y+r*np.cos(edge))
z = np.append(z,[c_z+h]*13)

print(z)
points = np.array(list(zip(x,y,z)))

for dim in [0,1,2]:
    dims = list(set([0,1,2])-set([dim]))
    lines = [0,0,0]
    for z in set(points[:, dim]):
        point = points[points[:, dim]==z]
        point = point[:, dims]
        center_0 = sum(point[:, 0]) / len(point)
        center_1 = sum(point[:, 1]) / len(point)
        point = np.array(sorted(point, key=lambda point: math.atan2(point[1]-center_1, point[0]-center_0)))
        point = np.array([*point,point[0]])
        #print(point)
        lines[dim] = [z]*len(point)
        lines[dims[0]] = point[:, 0]
        lines[dims[1]] = point[:, 1]
        ax.plot(*lines, 'b')

ax.set_xlim([points.min(), points.max()])
ax.set_ylim([points.min(), points.max()])
ax.set_zlim([points.min(), points.max()])
plt.show()