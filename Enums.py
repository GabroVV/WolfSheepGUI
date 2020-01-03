from enum import Enum
import random as rd


class Directions(Enum):
    North = 0
    East = 1
    South = 2
    West = 3

    @staticmethod
    def random_direction():
        return rd.choice([Directions.North, Directions.East, Directions.South, Directions.West])


class Status(Enum):
    Dead = 0
    Alive = 1
