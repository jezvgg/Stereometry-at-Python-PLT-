from figure import Figure
import numpy as np
from functools import total_ordering

@total_ordering
class Ellipsoid(Figure):
    __dots = np.array([])
    __square = 0
    __size = 0
    __color = ''


    def __init__(self, center_x: int = 0, center_y: int = 0, center_z: int = 0, 
                 a:int = 1, b:int = 1, c:int = 2, color: str = 'r'):
        self.__dots = self.dots(center_x, center_y, center_z, a, b, c)
        self.color = color
        self.__size = 4/3 * np.pi * a * b * c
        self.__square = 4*np.pi*((a**1.6*b**1.6+a**1.6*c*1.6+b**1.6*c**1.6)/3)**(1/1.6) 
    

    def dots(sself, center_x: int = 2, center_y: int = 2, center_z: int = 2, 
                 a:int = 1, b:int = 1, c:int = 1,):

        edge_n = 13
        z_n = 13
        edge = np.linspace(0, 2*np.pi, edge_n)
        x = np.array([])
        y = np.array([])
        z = np.array([])
        for Z in np.linspace(0, np.pi, z_n):
            x = np.append(x,center_x+a*np.sin(edge)*np.sin(Z))
            y = np.append(y,center_y+b*np.cos(edge)*np.sin(Z))
            z = np.append(z,[center_z+c*np.cos(Z)]*edge_n)

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
        