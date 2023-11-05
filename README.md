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
<picture>
 <source media="(prefers-color-scheme: dark)" srcset="https://imgur.com/XEEUPHm">
 <source media="(prefers-color-scheme: light)" srcset="(https://imgur.com/XEEUPHm)">
 <img alt="Cube Image" src="https://imgur.com/XEEUPHm">
</picture>
