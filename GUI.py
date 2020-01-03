from tkinter import *
from Wolf import Wolf

class GUI(object):
    def __init__(self, wolf):
        self.window = Tk()
        self.window.title("WolfSheepSimulation")
        self.window.geometry(str(3 * wolf.init_pos_limit) + 'x' + str(3 * wolf.init_pos_limit + 40))
        self.wolf = wolf
        self.canvas = Canvas(self.window, width=3 * wolf.init_pos_limit, height=3 * wolf.init_pos_limit, bg="#42F058")
        self.canvas.pack()
        self.canvas.bind("<Button-3>", self.right_click_callback)
        self.wolf_display = None
        self.render_wolf()

    def render_wolf(self):
        self.canvas.delete(self.wolf_display)
        x = self.wolf.coordinates[0]
        y = self.wolf.coordinates[1]
        radius = self.wolf.init_pos_limit * 0.05
        self.wolf_display = self.canvas.create_oval(x-radius, y-radius, x+radius, y+radius, fill="#FF0000", outline='')

    def right_click_callback(self,event):
        self.wolf.reset_wolf(event)
        self.render_wolf()




