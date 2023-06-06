# File: jewel_brick.py
# Description: Implementation of JewelBrick class
# Author: Chris Knowles


# Imports
from brick import Brick
from jewel import Jewel


# Consts
# Globals


# Classes
class JewelBrick(Brick):
    COLORS = {1: "#FFD700"}

    def __init__(self, game, x, y, points_value):
        super().__init__(game, x, y, 1, points_value)

    def remove(self):
        """
        Processes the removal of a jewel brick once it has been hit for its requisite number of available hits, this
        brick turns into an instance of a Jewel class

        :return: None
        """
        self.game.score += self.get_score()
        self.game.update_hud_text()
        x, y, _, _ = self.get_position()
        self.game.add_jewel(x + self.width / 2, y + self.height / 2, self.points_value)
        self.delete()
