from tkinter import *
from tkinter import messagebox
import random
import time

tk = Tk()
app_runimg = True

size_canas_x = 768
size_canas_y = 768


def on_closing():
    global app_runimg
    if messagebox.askokcancel("Выход из игры", "Хотите выйти из игры"):
        app_runimg = False
        tk.destroy()


tk.protocol("WM_DELETE_WINDOW", on_closing)

tk.title(" Игра крестики нолики")
tk.resizable(0, 0)
tk.attributes("-topmost", 1)
canvas = Canvas(tk, width=size_canas_x, height=size_canas_y,
                bd=0, highlightthickness=0)
canvas.pack()
tk.update()

s_x = 3
s_y = 3
step_x = size_canas_x // s_x
step_y = size_canas_y // s_y


def draw_table():
    for i in range(0, s_x + 1):
        canvas.create_line(0, i * step_y, size_canas_x, i * step_y)
    for i in range(0, s_y + 1):
        canvas.create_line(i * step_y, 0, i * step_y, size_canas_y)


points = []
draw_table()


class Point:
    def __init__(self, x, y, type):
        self.x = x
        self.y = y
        self.type = type

    def __str__(self):
        return str(self.__class__) + ":" + str(self.__dict__)


def draw_point(x, y, type):
    size = 25
    color = "black"
    if type == 0:
        color = "red"
    if type == 1:
        color = "blue"
        print(type)
        #id = canvas.create_oval(x * step_x, y * step_y, x * step_x + step_x, y * step_y + step_y, fill=color)


def add_to_points(event):
    print(event.num, event.x, event.y, type)
    type = 0
    if event.num == 3:
        type = 1
    points.append(Point(event.x // step_x, event.y // step_x, type))
    draw_point(event.x, event.y, type)
    print("".join(map(str, points)))


canvas.bind_all("Button-1", add_to_points)
canvas.bind_all("Button-1", add_to_points)

while app_runimg:
    if app_runimg:
        tk.update_idletasks()
        tk.update()
time.sleep(0.005)
