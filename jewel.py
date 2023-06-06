# File: jewel.py
# Description: Implementation of Jewel class
# Author: Chris Knowles


# Imports
from game_object import GameObject


# Consts
# Globals


# Classes
class Jewel(GameObject):
    COLOR = "#800080"

    def __init__(self, game, x, y, points_value):
        self.game = game
        self.width = 20
        self.height = 20
        self.points_value = points_value
        self.speed = 2
        color = type(self).COLOR
        item = self.game.canvas.create_polygon([x - self.width / 2, y,
                                                x, y - self.height / 2,
                                                x + self.width / 2, y,
                                                x, y + self.height / 2],
                                                fill=color, tags="jewel")

        super().__init__(self.game.canvas, item)

    def update(self):
        self.move(0, self.speed)

        bbox = self.game.canvas.bbox(self.item)
        items = self.game.canvas.find_overlapping(*bbox)

        if self.game.paddle.item in items:
            self.game.score += self.points_value
            self.game.update_hud_text()
            self.delete()
            return

        if self.get_position()[1] >= (self.game.paddle.get_position()[3] + 40):
            self.delete()

