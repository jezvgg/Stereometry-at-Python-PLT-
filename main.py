from Project.Canvas.canvasV2 import CanvasV2
from Project.Figures.cilinder import Cilinder
from Project.Figures.cube import Cube
from Project.Figures.parallelepiped import Parallelepiped
from Project.Figures.ellipsoid import Ellipsoid
from Project.Figures.sphere import Sphere

p = Parallelepiped(start_x=1)
cb = Cube(start_x=3, start_y=3, start_z=3, color='m')
el = Ellipsoid(center_x = 4)
sp = Sphere(color='y')
cl = Cilinder(center_z=3, h=3, r=2, color='g')
c = CanvasV2(cb,p,el,sp,cl)
c.show()