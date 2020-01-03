from tkinter import *
from Wolf import Wolf
from Sheep import Sheep


class GUI(object):
    def __init__(self, wolf):
        self.window = Tk()
        self.window.title("WolfSheepSimulation")
        self.window.geometry(str(3 * wolf.init_pos_limit) + 'x' + str(3 * wolf.init_pos_limit + 40))
        self.wolf = wolf
        self.canvas = Canvas(self.window, width=3 * wolf.init_pos_limit, height=3 * wolf.init_pos_limit, bg="#42F058")
        self.canvas.pack()
        self.canvas.bind("<Button-3>", self.right_click_callback)
        self.canvas.bind("<Button-1>", self.left_click_callback)

        self.wolf_display = None
        self.sheep_display = []

        self.render_wolf()

    def render_wolf(self):
        self.canvas.delete(self.wolf_display)
        x = self.wolf.coordinates[0]
        y = self.wolf.coordinates[1]
        radius = self.wolf.init_pos_limit * 0.05
        self.wolf_display = self.canvas.create_oval(x-radius, y-radius, x+radius, y+radius, fill="#FF0000", outline='')

    def render_sheep(self):
        radius = self.wolf.init_pos_limit * 0.05
        for sheep in self.wolf.sheep_list:
            self.sheep_display.append(self.canvas.create_oval(sheep.x - radius, sheep.y - radius, sheep.x + radius, sheep.y + radius, fill="#0000FF" , outline=''))

    def right_click_callback(self,event):
        self.wolf.reset_wolf(event)
        self.render_wolf()

    def left_click_callback(self,event):
        s = Sheep(0.5, event.x, event.y)
        self.wolf.sheep_list.append(s)
        self.render_sheep()




