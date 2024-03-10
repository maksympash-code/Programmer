from turtle import *
from Triangle_scaling import Triangle
from time import sleep


vertex_1 = [float(d) for d in input("Enter first vertex: ").split()]
vertex_2 = [float(d) for d in input("Enter second vertex: ").split()]
position = [float(d) for d in input("Enter position: ").split()]
scale = float(input("Enter scaling value bigger than 1: "))

triangle = Triangle(vertex_1, vertex_2)
triangle.set_scale_point(triangle.centroid())

up()
setpos(triangle.centroid())
down()
dot(4)
hideturtle()
triangle.draw()

scale_value = 1

while scale_value <= scale:
    triangle.set_scale(scale_value)
    triangle_turtle = triangle.draw()
    triangle_turtle.hideturtle()
    scale_value += 0.05
    sleep(0.1)

    if scale_value <= scale:
        triangle_turtle.clear()

mainloop()