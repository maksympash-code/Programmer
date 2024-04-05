from Figure import Figure
from turtle import *
from math import *
class Rectangle(Figure):
    def __init__(self,x1,y1,x2 = 0,y2 = 0):
        super().__init__()
        self._vertex1 = (x1,y1)
        self._vertex2 = (x2,y2)


    def draw(self):
        v1 = self.calc_abs_pos((self._vertex1[0], 0))
        v2 = self.calc_abs_pos(self._vertex1)
        v3 = self.calc_abs_pos((0 , self._vertex1[1]))
        color(self.color)
        up()
        setpos(*self.position)
        down()
        goto(*v1)
        goto(*v2)
        goto(*v3)
        setpos(*self.position)
        up()
        color(Rectangle.default_color)


if __name__ == '__main__':
    speed(0)
    triangle = Rectangle(100, 100)
    triangle.draw()

    for degree in range(1, 100):
        # triangle.set_rotation_degree(degree)


        triangle.draw()
        clear()

    mainloop()