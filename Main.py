from Sheep import Sheep
from Wolf import Wolf
from Enums import Status
from GUI import GUI
from tkinter import *

class Simulation(object):
    def __init__(self, turns, sheep_count, sheep_speed, wolf_speed, limit):
        self.turns = turns
        self.sheep_count = sheep_count
        self.sheep_speed = sheep_speed
        self.wolf_speed = wolf_speed
        self.limit = limit
        self.sheep_list = []
        self.wolf = Wolf(wolf_speed, self.sheep_list)
        self.turn = 1

    def simulate(self):
        for i in range(0, self.sheep_count):
            self.sheep_list.append(Sheep(i, self.sheep_speed, self.limit))
        while self.turn <= self.turns and self.sheep_left_check():
            for sheep in self.sheep_list:
                sheep.update()
            self.wolf.update()
            self.turn += 1

    def count_alive_sheep(self):
        count = 0
        for sheep in self.sheep_list:
            if sheep.status == Status.Alive:
                count += 1
        return count

    def sheep_left_check(self):
        for sheep in self.sheep_list:
            if sheep.status == Status.Alive:
                return True
        return False


if __name__ == "__main__":
    w = Wolf(1,300)
    gui = GUI(w)
    gui.render_wolf()
    canvas = Canvas(gui.window, width=3 * 300, height=3 * 300, bg="#42F058")
    gui.window.mainloop()

