from Node import *
class Ship(Node):
    def __init__(self, canvas,x1,y1):
        id = canvas.create_rectangle(0,0,x1,y1)
        super().__init__(id)

    def draw(self):
        pass
