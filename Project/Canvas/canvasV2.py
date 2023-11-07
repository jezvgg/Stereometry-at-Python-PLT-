from canvas import Canvas
import numpy as np
import math

class CanvasV2(Canvas):

    def __distance(self, point1: list, point2: list):
        return ((point2[0]-point1[0])**2 + (point2[1]-point1[1])**2 + (point2[2]-point1[2])**2)**0.5

    def _draw_figure(self, figure):
            points = figure.points
            color = figure.color
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
                    point1 = min(points[points[:, 2] > Z], key = lambda x: self.__distance(point, x))
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
                
            self._ax.plot(x, y, z, color)