# File: brick.py
# Description: Implementation of Brick class
# Author: Chris Knowles


# Imports
from game_object import GameObject


# Consts
# Globals


# Classes
class Brick(GameObject):
    COLORS = {1: "#999999", 2: "#555555"}

    def __init__(self, game, x, y, hits, points_value):
        self.game = game
        self.width = 75
        self.height = 20
        self.hits = hits
        self.points_value = points_value
        color = type(self).COLORS[hits]
        item = self.game.canvas.create_rectangle(x - self.width / 2,
                                                 y - self.height / 2,
                                                 x + self.width / 2,
                                                 y + self.height / 2,
                                                 fill=color, tags="brick")
        super().__init__(self.game.canvas, item)

    def hit(self):
        self.hits -= 1

        if self.hits == 0:
            self.remove()
        else:
            self.canvas.itemconfig(self.item,
                                   fill=type(self).COLORS[self.hits])

    def remove(self):
        """
        Processes the removal of a brick once it has been hit for its requisite number of available hits

        :return: None
        """
        self.game.score += self.get_score()
        self.game.update_hud_text()
        self.delete()

    def get_score(self):
        """
        Provides the points score for removing this brick or one of its subclasses

        :return: points scored for removing this brick, as integer
        """
        return self.points_value
