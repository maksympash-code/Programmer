from turtle import *
from math import *
from Triangle_rotated_with_rotation_matrix import Triangle



triangle = Triangle((10,50), (50,110))

triangle.set_position((0,0))
rotation_point = triangle.incenter()
triangle.set_rotation_point(rotation_point)

up()
setpos(rotation_point)
down()
dot(4)
hideturtle()

for i in range(0,363, 3):
    triangle.set_angle(i)
    triangle.draw()

mainloop()