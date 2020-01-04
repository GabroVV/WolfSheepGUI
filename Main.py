from Wolf import Wolf
from GUI import GUI
from tkinter import *




if __name__ == "__main__":
    w = Wolf(20,300)
    gui = GUI(w)
    gui.render_wolf()
    canvas = Canvas(gui.window, width=3 * 300, height=3 * 300, bg="#42F058")
    gui.window.mainloop()

