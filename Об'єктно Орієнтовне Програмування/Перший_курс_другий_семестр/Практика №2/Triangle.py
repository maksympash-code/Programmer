import turtle
from random import randint
from math import sin, cos,  radians

class Triangle:
    default_color = "#DF56AB"

    def __init__(self, x1, y1, x2, y2):
        self.vertex1 = (x1, y1)
        self.vertex2 = (x2, y2)
        self.color = Triangle.default_color
        self.rotation = 0
        self.position = (0, 0)
        self.scale = (1, 1)

    def set_position(self):
        self.position = (randint(-200, 200), randint(-200, 200))

    def set_color(self, color):
        self.color = color

    def coloring(self):
        red = randint(0, 255)
        green = randint(0, 255)
        blue = randint(0, 255)
        return "#{:02X}{:02X}{:02X}".format(red, green, blue)

    def calc_abs_pos(self):
        scaled_vertex1 = self.scaleVertex(self.vertex1, self.scale)
        scaled_vertex2 = self.scaleVertex(self.vertex2, self.scale)
        rotated_vertex1 = self.rotateVertex(scaled_vertex1, self.rotation)
        rotated_vertex2 = self.rotateVertex(scaled_vertex2, self.rotation)
        v1 = (self.position[0] + rotated_vertex1[0], self.position[1] + rotated_vertex1[1])
        v2 = (self.position[0] + rotated_vertex2[0], self.position[1] + rotated_vertex2[1])
        return v1, v2

    def scaleVertex(self, vertex, scale):
        return (scale[0] * vertex[0], scale[1] * vertex[1])

    def rotateVertex(self, vertex, angle):
        x = vertex[0] * cos(radians(angle)) - vertex[1] * sin(radians(angle))
        y = vertex[0] * sin(radians(angle)) + vertex[1] * cos(radians(angle))
        return (x, y)

    def draw(self):
        v1, v2 = self.calc_abs_pos()
        turtle.color(self.color)
        turtle.up()
        turtle.setpos(*self.position)
        turtle.down()
        turtle.goto(*v1)
        turtle.goto(*v2)
        turtle.setpos(*self.position)
        turtle.up()
        turtle.color(Triangle.default_color)

    def set_rotation_degree(self, degree):
        self.rotation = degree

    def set_scale(self, scale_x, scale_y):
        self.scale = (scale_x, scale_y)

if __name__ == '__main__':
    turtle.speed(0)
    triangle = Triangle(randint(-100, 100), randint(-100, 100), randint(-100, 100), randint(-100, 100))
    #triangle.draw()
    ch=0
    for degree in range(3, 363, 3):
        triangle.set_rotation_degree(degree)
        ch=ch+0.05
        scale_factor = ch + sin(radians(degree))
        triangle.set_scale(1, scale_factor)
        turtle.undo()
        triangle.draw()


    triangle.set_color("#38915F")
    for i in range(100):
        triangle = Triangle(randint(-100, 100), randint(-100, 100), randint(-100, 100), randint(-100, 100))
        turtle.begin_fill()
        triangle.set_color(triangle.coloring())
        triangle.set_position()
        triangle.draw()
        turtle.end_fill()

    turtle.done()