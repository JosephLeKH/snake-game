from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import ScoreBoard

# Setup Turtle screen
screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("My Snake Game")

# Turn animation update off, make it manual
screen.tracer(n=0)

snake = Snake()
food = Food()
sb = ScoreBoard()
gameOn = True

# Listen to inputs as the game progress
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

# Game keep playing until the user quit the game. If the game end automatically reset the game
while gameOn:
    # Update the game every 100ms
    screen.update()
    time.sleep(0.1)
    snake.move()

    # Detect food collision (if distance between head and food is less than 15px)
    if snake.head.distance(food) < 15:
        food.refresh()
        sb.refresh()
        snake.grow()

    # Detect collision with wall (if snake goes too far out)
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        sb.play_again()
        snake.refresh()

    # Detect collision with tail (if distance between head and part is less than 5px)
    for segment in snake.turtles[1:]:
        if snake.head.distance(segment) < 5:
            sb.play_again()
            snake.refresh()


screen.exitonclick()
