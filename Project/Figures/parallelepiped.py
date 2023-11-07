import numpy as np
from figure import Figure
from functools import total_ordering

@total_ordering
class Parallelepiped(Figure):
    __dots = np.array([])
    __square = 0
    __size = 0
    __color = ''


    def __init__(self, start_x: int = 0, start_y: int = 0, start_z: int = 0, 
                 a:int = 1, b:int = 1, h:int = 2, color: str = 'b'):
        self.__dots = self.dots(start_x, start_y, start_z,
                                a,b,h)
        self.__size = a*b*h
        self.__square = a*b*2 + a*h*2 + b*h*2
        self.color = color
    

    def __eq__(self, x: int):
        return self.size == x
    
    def __it__(self, x: int):
        return self.size < x
    
    def __gt__(self, x: int):
        return self.size > x


    def dots(self, start_x: int = 0, start_y: int = 0, start_z: int = 0, 
                 a:int = 1, b:int = 1, h:int = 2):
        return np.array([
            [start_x, start_y, start_z],
            [start_x+a, start_y, start_z],
            [start_x, start_y+b, start_z],
            [start_x+a, start_y+b, start_z],
            [start_x, start_y, start_z+h],
            [start_x+a, start_y, start_z+h],
            [start_x, start_y+b, start_z+h],
            [start_x+a, start_y+b, start_z+h]
        ])
    

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
        