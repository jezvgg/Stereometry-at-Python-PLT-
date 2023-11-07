from canvasV2 import CanvasV2
from parallelepiped import Parallelepiped
from cube import Cube
from ellipsoid import Ellipsoid
from sphere import Sphere
from cilinder import Cilinder

p = Parallelepiped(start_x=1)
cb = Cube(start_x=3, start_y=3, start_z=3, color='m')
el = Ellipsoid(center_x = 4)
sp = Sphere(color='y')
cl = Cilinder(center_z=3, h=3, r=2, color='g')
c = CanvasV2(max(cb,p,el,sp,cl))
c.show()