from turtle import *
from random import *
from math import *


class Triangle:
    def __init__(self, x1, y1, x2, y2):
        self.dot1 = (x1, y1)
        self.dot2 = (x2, y2)
        self.dot0 = (0, 0)
        self.color = self.random_color()

    @staticmethod
    def random_color():
        r = random()
        g = random()
        b = random()
        return r, g, b

    def calc_pos(self, vertex):
        x = self.dot0[0] + vertex[0]
        y = self.dot0[1] + vertex[1]
        return x, y

    def draw(self):
        color(self.color)
        v0 = self.calc_pos((randint(-300, 300), randint(-100, 100)))
        v1 = self.calc_pos(self.dot1)
        v2 = self.calc_pos(self.dot2)
        up()
        setpos(*v0)
        begin_fill()
        goto(*v1)
        goto(*v2)
        goto(*v0)
        end_fill()

    def rotate(self):
        triangle = Triangle(*self.dot1, *self.dot2)
        up()
        goto(0, 0)
        speed(0)
        v1 = [self.dot1[0], self.dot1[1]]
        v2 = [self.dot2[0] - self.dot1[0], self.dot2[1] - self.dot1[1]]
        v3 = [-self.dot2[0], -self.dot2[1]]
        len_1 = sqrt(v1[0] ** 2 + v1[1] ** 2)
        len_2 = sqrt(v2[0] ** 2 + v2[1] ** 2)
        len_3 = sqrt(v3[0] ** 2 + v3[1] ** 2)
        angle_1 = degrees(acos((v1[0] * v2[0] + v1[1] * v2[1]) / (len_1 * len_2)))
        angle_2 = degrees(acos((v2[0] * v3[0] + v2[1] * v3[1]) / (len_2 * len_3)))
        angle_3 = 180 - angle_1 - angle_2
        a = len_1
        b = a * sin(radians(angle_3)) / sin(radians(angle_2))
        c = a * sin(radians(angle_1)) / sin(radians(angle_2))
        fillcolor(random(), random(), random())
        for i in range(120):
            import time
            begin_fill()
            right(3)
            forward(a)
            left(180 - angle_1)
            forward(b)
            left(180 - angle_2)
            forward(c)
            left(180 - angle_3)
            end_fill()
            time.sleep(0.2)
            undo()


if __name__ == '__main__':
    speed(0)
    r = randint(0,100)
    for i in range(100):
        x1 = randint(-250, 250)
        y1 = randint(-50, 50)
        x2 = randint(-250, 250)
        y2 = randint(-75, 75)
        triangle = Triangle(x1, y1, x2, y2)
        if i == r:
            triangle.rotate()
        else:
            triangle.draw()

    mainloop()
