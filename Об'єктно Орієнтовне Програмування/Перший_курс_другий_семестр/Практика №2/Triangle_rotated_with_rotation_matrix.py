from math import *
import turtle


class Triangle:
    color = '#000000'

    def __init__(self, vertex_1, vertex_2):
        assert len(vertex_1) == 2 and len(vertex_2) == 2

        self._vertex_1 = vertex_1
        self._vertex_2 = vertex_2
        self._position = 0, 0
        self._speed = 0
        self._angle = 0
        self._rotation_point = self._position
        self._scale = 1
        self._scale_point = self._position
        self.list_of_vertexes = [(0, 0), vertex_1, vertex_2]

    def set_position(self, new_position: tuple):
        self._position = new_position

    def set_color(self, new_color: str):
        if new_color[0] == "#":
            assert len(new_color) == 7

        self.color = new_color

    def set_angle(self, new_angle):
        self._angle = new_angle

    def set_rotation_point(self, new_rotation_point):
        assert len(new_rotation_point) == 2

        self._rotation_point = new_rotation_point

    def set_scale(self, new_scale):
        assert new_scale > 0

        self._scale = new_scale

    def set_scale_point(self, new_scale_point):
        assert len(new_scale_point) == 2

        self._scale_point = new_scale_point

    def add_angle(self, input_angle: float):
        self._angle += input_angle

    def incenter(self):
        position, vertex_1, vertex_2 = self.calc_current_pos()

        a = self.vector_length(self.calc_vector(vertex_1, vertex_2))      # a - position
        b = self.vector_length(self.calc_vector(position, vertex_2))      # b - vertex_1
        c = self.vector_length(self.calc_vector(position, vertex_1))      # c - vertex_2

        incenter = ((a * position[0] + b * vertex_1[0] + c * vertex_2[0]) / (a + b + c),
                    (a * position[1] + b * vertex_1[1] + c * vertex_2[1]) / (a + b + c))

        return incenter

    @staticmethod
    def calc_vector(head, root):
        return head[0] - root[0], head[1] - root[1]

    @staticmethod
    def move_point(point, new_position):
        return point[0] + new_position[0], point[1] + new_position[1]

    @staticmethod
    def vector_length(vector):
        return (vector[0] ** 2 + vector[1] ** 2) ** 0.5

    def inner_angle(self, index: int, in_radians=False):
        assert 0 <= index <= 2

        list_of_vertexes = self.list_of_vertexes.copy()
        vertex = list_of_vertexes[index]
        list_of_vertexes.remove(vertex)

        vertex_a, vertex_b = list_of_vertexes

        vector_a = self.calc_vector(vertex_a, vertex)
        vector_b = self.calc_vector(vertex_b, vertex)
        a, b = self.vector_length(vector_a), self.vector_length(vector_b)

        cos_ab = (vector_a[0] * vector_b[0] + vector_a[1] * vector_b[1]) / (a * b)
        angle_radians = acos(cos_ab)

        if in_radians:
            return angle_radians

        return degrees(angle_radians)

    @staticmethod
    def calc_point_rotation(angle: float, point: tuple, rotation_point=(0, 0)):
        theta = radians(angle)
        vector = Triangle.calc_vector(point, rotation_point)
        rotated_vector = (vector[0] * cos(theta) + vector[1] * sin(theta),
                          -vector[0] * sin(theta) + vector[1] * cos(theta))

        return Triangle.move_point(rotated_vector, rotation_point)

    @staticmethod
    def calc_point_scale(scale: float, point: tuple, rotation_point=(0, 0)):
        vector = Triangle.calc_vector(point, rotation_point)
        scaled_vector = vector[0] * scale, vector[1] * scale

        return Triangle.move_point(scaled_vector, rotation_point)

    def calc_current_pos(self):
        position, vertex_1, vertex_2 = self._position, self._vertex_1, self._vertex_2
        scale_point, scale = self._scale_point, self._scale
        rotation_point, angle = self._rotation_point, self._angle

        scaled_position = self.calc_point_scale(scale, position, scale_point)
        scaled_vertex_1 = self.calc_point_scale(scale, vertex_1)
        scaled_vertex_2 = self.calc_point_scale(scale, vertex_2)

        current_position = self.calc_point_rotation(angle, scaled_position, rotation_point)
        rotated_vertex_1 = self.calc_point_rotation(angle, scaled_vertex_1)
        rotated_vertex_2 = self.calc_point_rotation(angle, scaled_vertex_2)

        current_vertex_1 = self.move_point(rotated_vertex_1, current_position)
        current_vertex_2 = self.move_point(rotated_vertex_2, current_position)

        return current_position, current_vertex_1, current_vertex_2

    def draw(self):
        triangle = turtle.Turtle()

        triangle.speed(self._speed)
        triangle.color(self.color)

        current_position, current_vertex_1, current_vertex_2 = self.calc_current_pos()

        triangle.up()
        triangle.setpos(current_position)
        triangle.down()
        triangle.goto(current_vertex_1)
        triangle.goto(current_vertex_2)
        triangle.setpos(current_position)
        triangle.up()

        triangle.hideturtle()

        return triangle
