from Figure import Figure
from turtle import *
from math import *
class Circle(Figure):
    def __init__(self, r):
        super().__init__()
        self._r = r


    def draw(self):
        s = self._r * self.scale[1]
        v1 = self.position[0],self.position[1] - s
        color(self.color)
        up()
        setpos(*self.position)
        down()
        circle(s)
        up()
        color(Circle.default_color)


if __name__ == '__main__':
    speed(0)
    triangle = Circle(100)
    triangle.draw()

    for degree in range(1, 100):
        # triangle.set_rotation_degree(degree)


        triangle.draw()
        clear()

    mainloop()