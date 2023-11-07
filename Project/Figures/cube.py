from Project.Figures.parallelepiped import Parallelepiped

class Cube(Parallelepiped):

    def __init__(self, start_x: int = 0, start_y: int = 0, start_z: int = 0, 
                 a:int = 1, color: str = 'b'):
        super().__init__(start_x=start_x, start_y=start_y, start_z=start_z,
                         a=a, b=a, h=a, color=color)
