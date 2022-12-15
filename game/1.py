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
step_x=size_canas_x//s_x
step_y=size_canas_y//s_y


def draw_table():
    for i in range(0, s_x):
        canvas.create_line(0, i*step_y, size_canas_x, i*step_y)
draw_table()



while app_runimg:
    if app_runimg:
        tk.update_idletasks()
        tk.update()
time.sleep(0.005)
