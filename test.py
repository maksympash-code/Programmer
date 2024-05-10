import tkinter as tk
import random

class Tank:
    def __init__(self, canvas, x, y, size, color, move_speed):
        self.canvas = canvas
        self.size = size
        self.move_speed = move_speed
        self.rect = canvas.create_rectangle(x, y, x + size, y + size, fill=color)

    def move(self, dx, dy):
        self.canvas.move(self.rect, dx, dy)

class Game:
    def __init__(self, master):
        self.master = master
        self.canvas = tk.Canvas(master, bg="white", width=800, height=600)
        self.canvas.pack()
        self.player_tank = Tank(self.canvas, 50, 50, 50, "blue", 5)
        self.enemy_tank = Tank(self.canvas, 700, 500, 50, "red", 2)
        self.master.bind("<KeyPress>", self.move_player)
        self.move_enemy()

    def move_player(self, event):
        key = event.keysym
        dx, dy = 0, 0
        if key == "Up":
            dy = -self.player_tank.move_speed
        elif key == "Down":
            dy = self.player_tank.move_speed
        elif key == "Left":
            dx = -self.player_tank.move_speed
        elif key == "Right":
            dx = self.player_tank.move_speed
        self.player_tank.move(dx, dy)

    def move_enemy(self):
        dx, dy = random.choice([-5, 5]), random.choice([-5, 5])
        self.enemy_tank.move(dx, dy)
        self.master.after(1000, self.move_enemy)

root = tk.Tk()
game = Game(root)
root.mainloop()
