# Handle the food in the game
from turtle import Turtle
import random as r

class Food(Turtle):

    # Create the food object as a Turtle subclass
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("red")
        self.speed("fastest")
        self.refresh()

    # Go to a random position within bound
    def refresh(self):
        self.goto(r.randint(-260, 260), r.randint(-260, 260))
