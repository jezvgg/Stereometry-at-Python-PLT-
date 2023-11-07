from Project.Figures.figure import Figure
import numpy as np

class Cilinder(Figure):
    __dots = np.array([])
    __square = 0
    __size = 0
    __color = ''


    def __init__(self, center_x: int = 0, center_y: int = 0, center_z: int = 0, 
                 r:int = 1, h:int = 2, color: str = 'g'):
        self.__dots = self.dots(center_x, center_y, center_z, r, h)
        self.color = color

    

    def dots(sself, center_x: int = 2, center_y: int = 2, center_z: int = 2, 
                 r:int = 1, h:int = 1):

        edge_n = 20
        edge = np.linspace(0, 2*np.pi, edge_n)
        x = np.array([])
        y = np.array([])
        z = np.array([])
        x = np.append(x,center_x+r*np.sin(edge))
        y = np.append(y,center_y+r*np.cos(edge))
        z = np.append(z,[center_z]*edge_n)
        x = np.append(x,center_x+r*np.sin(edge))
        y = np.append(y,center_y+r*np.cos(edge))
        z = np.append(z,[center_z+h]*edge_n)

        return np.array(list(zip(x,y,z)))
    

    @property
    def points(self):
        return self.__dots


    @property
    def size(self):
        return self.__size


    @property
    def square(self):
        return self.__square


    @property
    def color(self):
        return self.__color
    

    @color.setter
    def color(self, c):
        self.__color = c
