# File: bonus_brick.py
# Description: Implementation of BonusBrick class
# Author: Chris Knowles


# Imports
from brick import Brick


# Consts
# Globals


# Classes
class BonusBrick(Brick):
    COLORS = {1: "#FF0000"}

    def __init__(self, game, x, y, points_value):
        super().__init__(game, x, y, 1, points_value)
