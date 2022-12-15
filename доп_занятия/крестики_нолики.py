from tkinter import *
from tkinter import messagebox
import sys
import time
import random

tk = Tk()
app_runing = True


def on_closing():
    global app_runing
    if messagebox.askokcancel("Quit", "Do you want to quit?"):
        app_runing = False
        tk.destroy()


tk.protocol("WM_DELETE_WINDOW", on_closing)

tk.title("Крестики нолики")
tk.resizable(0, 0)
tk.wm_attributes("-topmost", 1)
canvas = Canvas(tk, width=800, height=768, bd=0, highlightthickness=0)
canvas.pack()
tk.update()

while 1:
 if app_runing:
  tk.update_idletasks()
  tk.update() 
time.sleep(0.005)  
