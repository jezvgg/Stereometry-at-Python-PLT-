from Project.Canvas import CanvasV2
from Project.Figures import *

p = Parallelepiped(start_x=1)
cb = Cube(start_x=3, start_y=3, start_z=3, color='m')
el = Ellipsoid(center_x = 4)
sp = Sphere(color='y')
cl = Cilinder(center_z=3, h=3, r=2, color='g')
c = CanvasV2(max(cb,p,el,sp,cl))
c.show()