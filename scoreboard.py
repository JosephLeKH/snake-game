# Handle the scoreboard graphics
from turtle import Turtle


# Font of the game
FONT = ("Courier", 20, "normal")


class ScoreBoard(Turtle):

    # Initialize the graphics and high score from data.txt
    def __init__(self):
        super().__init__()
        with open("data.txt") as file:
            self.high_score = int(file.read())
        self.score = 0
        self.penup()
        self.hideturtle()
        self.speed("fastest")
        self.color("white")
        self.goto(0, 270)
        self.write(f"Score: {self.score}  High Score: {self.high_score}", move=False, align="center", font=FONT)

    # Increase the score and refresh the graphic
    def refresh(self):
        self.clear()
        self.score += 1
        self.write(f"Score: {self.score}  High Score: {self.high_score}", move=False, align="center", font=FONT)

    # Update the high score, reset the score, and refresh the graphic
    def play_again(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode="w") as file:
                file.write(str(self.high_score))
        with open("data.txt") as file:
            self.high_score = int(file.read())
        self.score = 0
        self.clear()
        self.write(f"Score: {self.score}  High Score: {self.high_score}", move=False, align="center", font=FONT)
