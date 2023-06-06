# File: game.py
# Description: Implementation of Game class
# Author: Chris Knowles


# Imports
import tkinter as tk
from ball import Ball
from paddle import Paddle
from brick import Brick
from bonus_brick import BonusBrick
from jewel_brick import JewelBrick
from jewel import Jewel


# Consts
# Globals


# Classes
class Game(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.score = 0
        self.lives = 3
        self.width = 610
        self.height = 400
        self.canvas = tk.Canvas(self, bg="#aaaaff",
                                width=self.width,
                                height=self.height,)
        self.canvas.pack()
        self.pack()

        self.items = {}
        self.ball = None
        self.paddle = Paddle(self.canvas, self.width/2, 326)
        self.items[self.paddle.item] = self.paddle

        for x in range(5, self.width - 5, 75):
            self.add_brick("BRICK", x + 37.5, 50, 2)

            if x == 230:  # Make first middle brick a bonus bricks
                self.add_brick("BONUS_BRICK", x + 37.5, 70)
            elif x == 305:  # Make second middle brick a jewel bricks
                self.add_brick("JEWEL_BRICK", x + 37.5, 70)
            else:
                self.add_brick("BRICK", x + 37.5, 70)

            self.add_brick("BRICK", x + 37.5, 90)

        self.text = None
        self.hud = None
        self.setup_game()
        self.canvas.focus_set()

        self.canvas.bind("<Left>",
                         lambda _: self.paddle.move(-10))
        self.canvas.bind("<Right>",
                         lambda _: self.paddle.move(10))

    def setup_game(self):
        self.add_ball()
        self.update_hud_text()
        self.text = self.draw_text(300, 200,
                                   "Press Space to start")
        self.canvas.bind("<space>", lambda _: self.start_game())

    def add_ball(self):
        if self.ball is not None:
            self.ball.delete()

        paddle_coords = self.paddle.get_position()
        x = (paddle_coords[0] + paddle_coords[2]) * 0.5
        self.ball = Ball(self.canvas, x, 310)
        self.paddle.set_ball(self.ball)

    def add_brick(self, brick_type, x, y, hits=1):
        if brick_type == "BRICK":
            brick = Brick(self, x, y, hits, 100)
        elif brick_type == "BONUS_BRICK":
            brick = BonusBrick(self, x, y, 500)
        elif brick_type == "JEWEL_BRICK":
            brick = JewelBrick(self, x, y, 250)
        else:
            return  # Cannot add this type of brick

        self.items[brick.item] = brick

    def add_jewel(self, x, y, points_value):
        jewel = Jewel(self, x, y, points_value)
        self.items[jewel.item] = jewel

    def draw_text(self, x, y, text, size="40"):
        font = ("Helvetica", size)
        return self.canvas.create_text(x, y, text=text,
                                       font=font)

    def update_hud_text(self):
        text = "Lives: {0}                                                    Score: {1}".format(self.lives, self.score)

        if self.hud is None:
            self.hud = self.draw_text(310, 20, text, 15)
        else:
            self.canvas.itemconfig(self.hud, text=text)

    def start_game(self):
        self.canvas.unbind("<space>")
        self.canvas.delete(self.text)
        self.paddle.ball = None
        self.game_loop()

    def game_loop(self):
        self.check_collisions()
        num_bricks = len(self.canvas.find_withtag("brick"))

        if num_bricks == 0:
            self.ball.speed = None
            self.draw_text(300, 200, "You win!")
        elif self.ball.get_position()[3] >= self.height:
            self.ball.speed = None
            self.lives -= 1

            if self.lives < 0:
                self.draw_text(300, 200, "Game Over")
            else:
                self.after(1000, self.setup_game)
        else:
            if len(self.canvas.find_withtag("jewel")):
                jewel = self.items[self.canvas.find_withtag("jewel")[0]]
                jewel.update()

            self.ball.update()
            self.after(50, self.game_loop)

    def check_collisions(self):
        ball_coords = self.ball.get_position()
        items = self.canvas.find_overlapping(*ball_coords)
        objects = [self.items[x] for x in items if x in self.items]
        self.ball.collide(objects)
