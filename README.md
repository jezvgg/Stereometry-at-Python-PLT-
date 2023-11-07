# Stereometry-at-Python-PLT
Initially, this project was a simple homework at my university. The task was to make an abstract Figure class and inherit other shapes from it: a cube, a parallelipiped, a ball, an ellipsoid and a cylinder. In the process, I became interested in drawing them using graphs and making a class in which you can pass as many shapes as you want to draw them.

Then there were 2 ways to make my idea. Or write instructions for drawing each object individually, inside the class. Or write a universal function for drawing any shape based on its points. Accordingly, each class must count its points in space and return them.

Inside other.py I experimented and decided to make the following algorithm:
1. We pass through one of the 3 dimensions.
2. If we have points in the measurement slice, connect them clockwise.
3. Repeat for another measurement.

Despite the fact that everything seems to work well, I have problems with drawing ellipsoids. There are plans to rewrite the function of drawing a figure so that it determines the distance between points and connects the nearest ones. If it doesn't work out that way, then I will make a factory.

Here are some examples of work:

```python
from canvas import Canvas
from cube import Cube

cb = Cube(start_x=3, start_y=3, start_z=3, color='m')
c = Canvas(cb)
c.set_limits([0,7], [0,7], [0,7])
c.show()
```
![Cube Image](https://github.com/jezvgg/Stereometry-at-Python-PLT-/assets/40557881/c496603b-d985-4753-a6a4-029345d2e812)

Lots of shapes:
```python
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
```
![Figure_9](https://github.com/jezvgg/Stereometry-at-Python-PLT-/assets/40557881/e479941e-774b-4d75-b7d1-192627c2a8be)


But the algorithm for constructing figures turned out to be ineffective. He's not good at drawing ellipsoids. I decided to try to redo it using the principle of nearest neighbors. Canvas with this principles, now CanvasV2.
This picture shows the difference between Canvas and CanvasV2.
![Figure_11](https://github.com/jezvgg/Stereometry-at-Python-PLT-/assets/40557881/f104a7cb-d624-4f02-a58d-62063444ea52)
As you can see, the new algorithm, although it removed the creation of edges inside the ball, but it works just as badly.

As a result, I decided to combine both of these algorithms. If you take slices on only one axis and connect them, and then connect the slices using the nearest neighbors. Then we get a good result.
![Figure_12](https://github.com/jezvgg/Stereometry-at-Python-PLT-/assets/40557881/02957046-b275-4b78-8609-0364fff82c4d)
