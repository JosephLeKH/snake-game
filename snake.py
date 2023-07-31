# Handle the snake object in the game
from turtle import Turtle
MOVE_DISTANCE = 20


class Snake:

    # Set the 1st object in the item as the head of the snake
    def __init__(self):
        self.turtles = []
        self.create_snake()
        self.head = self.turtles[0]

    # Initialize the snake as a list of square turtle objects
    def create_snake(self):
        x = 0
        for i in range(3):
            tim = Turtle("square")
            tim.color("white")
            tim.penup()
            tim.goto(x, 0)
            self.turtles.append(tim)
            x -= 20

    # Move the snake off the game and create a new snake
    def refresh(self):
        for tim in self.turtles:
            tim.goto(1000, 1000)
        self.turtles.clear()
        self.create_snake()
        self.head = self.turtles[0]

    # Create an extra square, add it to the list, and move it to the tail
    def grow(self):
        tim = Turtle("square")
        tim.color("white")
        tim.penup()
        tim.goto(self.turtles[-1].pos())
        self.turtles.append(tim)

    # After the heading is set, move the head forward, and move every squares to the next square's pos
    def move(self):
        for i in range(len(self.turtles) - 1, 0, -1):
            self.turtles[i].goto(self.turtles[i - 1].pos())
        self.turtles[0].forward(MOVE_DISTANCE)

    # Set the direction of the snake, making sure it can't double back on itself
    def up(self):
        if self.head.heading() % 180 == 0:
            self.head.setheading(90)

    def down(self):
        if self.head.heading() % 180 == 0:
            self.head.setheading(270)

    def left(self):
        if self.head.heading() % 180 != 0:
            self.head.setheading(180)

    def right(self):
        if self.head.heading() % 180 != 0:
            self.head.setheading(0)

