# File: main.py
# Description: Implementation of (rather slow) Breakout clone using Tkinter,
#              a pygame or pyglet implementation would improve this of course
# Author: Chris Knowles


# Imports
import tkinter as tk
from game import Game

# Consts
# Globals
# Classes


# Program entry function
def main():
    """
    Main function, contains creation of Tkinter root window, Game class instance and main game loop

    :return: None
    """
    root = tk.Tk()
    root.title("Breakout!")
    game = Game(root)
    game.mainloop()


# Invoke main() program entrance
if __name__ == "__main__":
    # execute only if run as a script
    main()
