from Node import *


class Ship(Node):
    def __init__(self, canvas, x1, y1):
        id = canvas.create_rectangle(0, 0, x1, y1)
        super().__init__(id)

    def setPosition(self,x,y):
        self.pos = (x,y)

    def update(self):
        pass

    def draw(self):
        pass
