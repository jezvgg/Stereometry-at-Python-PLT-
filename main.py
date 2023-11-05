from canvas import Canvas
from parallelepiped import Parallelepiped
from cube import Cube
from ellipsoid import Ellipsoid
from sphere import Sphere
from cilinder import Cilinder

p = Parallelepiped(start_x=1)
cb = Cube(start_x=3, start_y=3, start_z=3, color='m')
el = Ellipsoid(center_x = 4)
sp = Sphere(center_y=5, color='y')
cl = Cilinder(center_z=3, h=3, r=2, color='g')
c = Canvas(el, sp, cl, p, cb)
c.set_limits([-5,7], [-5,7], [-5,7])
c.show()