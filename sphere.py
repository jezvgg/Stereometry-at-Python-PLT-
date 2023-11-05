from ellipsoid import Ellipsoid

class Sphere(Ellipsoid):

    def __init__(self, center_x: int = 0, center_y: int = 0, center_z: int = 0,
                 r: int = 1, color: str = 'r'):
        super().__init__(center_x, center_y, center_z, a=r, b=r, c=r, color=color)
