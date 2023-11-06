import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import math

class Canvas:
    '''
    Canvas to show figures in 3D
    '''
    __fig = plt.figure()
    _ax = plt.subplot(111, projection='3d')
    x = 100
    y = 100
    z = 100


    def __init__(self, *args: list):
        self.append(*args)

    
    def append(self, *args: list):
        lim = max(args, key=lambda x: x.points.max()).points.max()
        self.set_limits(5, 5, 5)
        for arg in args:
            self._draw_figure(arg)


    def _draw_figure(self, figure):
        points = figure.points
        color = figure.color 
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
                lines[dim] = [z]*len(point)
                lines[dims[0]] = point[:, 0]
                lines[dims[1]] = point[:, 1]
                self._ax.plot(*lines, color)


    def set_limits(self, x,y,z):
        self._ax.set_xlim(x)
        self._ax.set_ylim(y)
        self._ax.set_zlim(z)


    def show(self):
        plt.show()
