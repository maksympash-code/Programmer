from turtle import *
from random import *
from math import *


class Triangle:
    def __init__(self, x1, y1, x2, y2):
        self._vertex1 = (x1, y1)
        self._vertex2 = (x2, y2)
        self._position = (0, 0)
        self.color = self.random_color()

    @staticmethod
    def random_color():
        r = random()
        g = random()
        b = random()
        return r, g, b

    def calc_pos(self, vertex):
        x = self._position[0] + vertex[0]
        y = self._position[1] + vertex[1]
        return x, y

    def draw(self):
        setheading(0)
        color(self.color)
        v0 = self.calc_pos((randint(-300, 300), randint(-100, 100)))
        v1 = self.calc_pos(self._vertex1)
        v2 = self.calc_pos(self._vertex2)
        up()
        setpos(*v0)
        begin_fill()
        goto(*v1)
        goto(*v2)
        goto(*v0)
        end_fill()

    def rotate_vec(self, v1, a):
        x, y = v1
        a = radians(a)
        return (cos(a) * x - sin(a) * y, sin(a) * x + cos(a) * y)

    def rotate(self, a):
        self._vertex1 = self.rotate_vec(self._vertex1, a)
        self._vertex2 = self.rotate_vec(self._vertex2, a)


if __name__ == '__main__':
    speed(0)
    bgcolor(0.2, 0.2, 0.2)
    r = randint(0, 100)
    for i in range(100):
        x = []
        y = []
        for j in range(2):
            x.append(randint(-200, 200))
            y.append(randint(-50, 50))
        triangle = Triangle(x[0], y[0], x[1], y[1])
        if i == r:
            triangle.rotate()
        else:
            triangle.draw()
        mainloop()
