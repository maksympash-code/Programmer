from tkinter import *

def sayHello(event):
    print("Hello,World!!!")
    btn["text"] = "Hello,World!!!"

root = Tk()
root.title("Tanks")

canvas = Canvas(root, width=500, height=500)
canvas.pack()

btn = Button(root,
             text="Click Me",
             width=20, height=10,
             bg = "yellow", fg = "blue",
             font = "Arial 18")


btn.bind("<Button-1>", sayHello)
btn.pack()
root.geometry("800x600")




root.mainloop()