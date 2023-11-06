from canvas import Canvas
import numpy as np

class CanvasV2(Canvas):

    def __distance(self, point1: list, point2: list):
        return ((point2[0]-point1[0])**2 + (point2[1]-point1[1])**2 + (point2[2]-point1[2])**2)**0.5

    def _draw_figure(self, figure):
        points = figure.points
        color = figure.color 
        neightbors = 5
        x = np.array([])
        y = np.array([])
        z = np.array([])
        for point in points:
            for point2 in sorted(points, key=lambda x: self.__distance(x, point))[:neightbors]:
                x = np.append(x, np.array([point[0], point2[0]]))
                y = np.append(y, np.array([point[1], point2[1]]))
                z = np.append(z, np.array([point[2], point2[2]]))
        self._ax.plot(x, y, z, color)