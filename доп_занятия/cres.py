from tkinter import *

window = Tk()
window.geometry('600x600')
window.title('Крестики нолики')

# t=Button(text="x", font=("Comic Sans MS", 24,"bold"))
# t.place(x=0, y=0, width=120, height=120)
w = 120
class Btn():
    global w
    def _init_(self, x0, y0):
        self.x0 = x0
        self.y0 = y0
        self.Button1 = Button().place(x=self.x0, y=self.y0, width=120, height=120)
    def show(self):
        x = 0
        y = 0
        for i in range(3):
            for j in range(3):
                Btn(x, y)
                x += W
        x = 0
        y += w


Btn()
window.mainloop()
