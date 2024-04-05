from Figure import Figure
from Triangle import Triangle
from Rectangle import Rectangle
from Circle import Circle
from turtle import *

class Car(Figure):
    def __init__(self):
        super().__init__()
        self.components = []

    def add_component(self, component):
        self.components.append(component)

    def draw(self):
        for component in self.components:
            component.position = self.position

        for component in self.components:
            component.draw()

if __name__ == '__main__':
    body = Rectangle(200, 100)
    window = Triangle(100, 0, 50, 100)
    window.set_position(50, 100)

    wheel1 = Circle(20)
    wheel2 = Circle(20)

    wheel1.set_position(35, -40)
    wheel2.set_position(165, -40)

    car = Car()
    car.add_component(body)
    car.add_component(window)
    car.add_component(wheel1)
    car.add_component(wheel2)

    for step in range(1,100):
        car.set_position(step, 0)
        car.draw()
        clear()