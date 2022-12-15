from tkinter import *
import sys

root = Tk()
root.title("lesson")
root.geometry("500x300+700+500")
root.resizable(width=False, height=False)

l=Label(text="Text")
e=Entry()
b=Button(text="ok")

l.grid(row=1, column=1)
e.grid(row=2, column=1)
b.grid(row=3, column=1)

l.pack()
e.pack()
b.pack()

# grid() pack()

root.mainloop()