from tkinter import *
from Wolf import Wolf
from Sheep import Sheep
from Enums import Status
import tkinter.font as TkFont

class GUI(object):
    def __init__(self, wolf,counter):
        self.window = Tk()
        self.frame = Frame(self.window)
        self.frame.pack()
        self.counter = counter

        self.window.title("WolfSheepSimulation")
        self.window.geometry(str(3 * wolf.init_pos_limit) + 'x' + str(3 * wolf.init_pos_limit + 40))
        self.wolf = wolf
        self.canvas = Canvas(self.window, width=3 * wolf.init_pos_limit, height=3 * wolf.init_pos_limit, bg="#42F058")
        self.canvas.pack(side = BOTTOM)
        self.canvas.bind("<Button-3>", self.right_click_callback)
        self.canvas.bind("<Button-1>", self.left_click_callback)
        self.canvas.bind("<Button-2>", self.step_callback)
        self.canvas.bind("<Button-4>", self.reset_callback)
        self.widget = Label(self.window, text="Liczba zywych owiec: " + str(self.counter), fg='black', bg="#ffffcc")
        self.widget.pack(side = LEFT)
        self.step_button = Button(self.window, text="Step", command = self.step_callback)
        self.step_button.configure(width=10, activebackground="#33B5E5", relief=FLAT, bg="#ffffcc")
        self.step_button.pack(side = RIGHT)
        self.reset_button = Button(self.window, text="Reset", command = self.reset_callback)
        self.reset_button.configure(width=10, activebackground="#33B5E5", relief=FLAT, bg="#ffffcc")
        self.reset_button.pack(side = RIGHT)
        self.wolf_display = None
        self.sheep_display = []
        self.render_wolf()

    def render_wolf(self):
        self.canvas.delete(self.wolf_display)
        x = self.wolf.coordinates[0]
        y = self.wolf.coordinates[1]
        radius = self.wolf.init_pos_limit * 0.05
        self.wolf_display = self.canvas.create_oval(x-radius, y-radius, x+radius, y+radius, fill="#FF0000", outline='')

    def update_label(self):
        self.counter = self.wolf.count_alive_sheep()
        # self.canvas.create_window(100, 100, window=self.widget)
        self.widget.pack_forget()
        self.widget.destroy()
        self.widget = Label(self.window, text="Liczba zywych owiec: " + str(self.counter), fg='black', bg="#ffffcc")
        self.widget.pack(side=LEFT)




    def render_sheep(self):
        self.canvas.delete(self.sheep_display)
        radius = self.wolf.init_pos_limit * 0.05
        for sheep in self.wolf.sheep_list:
            if sheep.status == Status.Alive:
                x = sheep.coordinates[0]
                y = sheep.coordinates[1]
                self.sheep_display.append(self.canvas.create_oval(x - radius, y - radius, x + radius, y + radius, fill="#0000FF" , outline=''))
        self.update_label()

    def right_click_callback(self,event):
        self.wolf.reset_wolf(event)
        self.render_wolf()

    def left_click_callback(self,event):
        s = Sheep(10, event.x, event.y)
        self.wolf.sheep_list.append(s)
        self.render_sheep()

    def step_callback(self):
        if self.sheep_left_check():
            self.canvas.delete("all")
            self.wolf.update()
            for sheep in self.wolf.sheep_list:
                sheep.update()
            self.render_wolf()
            self.render_sheep()
        else:
            print(TkFont.families())
            font = TkFont.Font(size=20)
            end_window = Tk()
            end_window.title("Error")
            end_window.geometry("250x30")
            label = Message(end_window,font=font, text="All sheep are dead, can't step", width=1000)
            label.pack()
            end_window.mainloop()

    def reset_callback(self):
        for sheep in self.wolf.sheep_list:
            if sheep.status == Status.Alive:
                sheep.die()
        self.canvas.delete("all")
        self.render_wolf_in_the_middle()
        self.update_label()

    def render_wolf_in_the_middle(self):
        self.wolf.coordinates[0]=(3 * self.wolf.init_pos_limit)/2
        self.wolf.coordinates[1]=(3 * self.wolf.init_pos_limit)/2
        x = (3 * self.wolf.init_pos_limit)/2
        y = (3 * self.wolf.init_pos_limit)/2
        radius = self.wolf.init_pos_limit * 0.05
        self.wolf_display = self.canvas.create_oval(x - radius, y - radius, x + radius, y + radius, fill="#FF0000", outline='')



    def sheep_left_check(self):
        for sheep in self.wolf.sheep_list:
            if sheep.status == Status.Alive:
                return True
        return False







