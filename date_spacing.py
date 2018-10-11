# Module made for calculation of space between date-ticks on plot easier
import math


def calculate(data):
    return math.floor(len(data) ** (1/3))
