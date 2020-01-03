import math
import Sheep


class Wolf(object):
    def __init__(self, speed, sheep_list):
        self.coordinates = [0.0, 0.0]
        self.wolf_move_dist = speed
        self.sheep_list = sheep_list

    def distance(self, sheep):
        difference_x = self.coordinates[0] - sheep.coordinates[0]
        difference_x *= difference_x
        difference_y = self.coordinates[1] - sheep.coordinates[1]
        difference_y *= difference_y
        distance = math.sqrt(difference_y + difference_x)
        return distance

    def first_alive_sheep_index(self):
        for i in range(len(self.sheep_list)):
            if self.sheep_list[i].status == Sheep.Status.Alive:
                return i
        return len(self.sheep_list)  # returns a dead sheep index if all sheep are dead

    def find_closest_sheep(self):
        closest_sheep_index = self.first_alive_sheep_index()
        min_distance = self.distance(self.sheep_list[closest_sheep_index])
        for i in range(len(self.sheep_list)):
            dist = self.distance(self.sheep_list[i])
            if dist < min_distance and self.sheep_list[i].status == Sheep.Status.Alive:
                closest_sheep_index = i
                min_distance = dist
        return min_distance, closest_sheep_index

    def update(self):
        distance, index = self.find_closest_sheep()
        closest_sheep = self.sheep_list[index]
        if distance < self.wolf_move_dist:
            closest_sheep.die()
        else:
            self.move_towards_sheep(closest_sheep)

    def move_towards_sheep(self, sheep):
        vector = [sheep.coordinates[0] - self.coordinates[0], sheep.coordinates[1] - self.coordinates[1]]
        length = math.sqrt(vector[0]*vector[0] + vector[1]*vector[1])
        self.coordinates[0] += self.wolf_move_dist*vector[0]/length
        self.coordinates[1] += self.wolf_move_dist*vector[1]/length
