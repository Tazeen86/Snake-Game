from turtle import Turtle,Screen
from scoreboard import Scoreboard
from snake import Snake
from food import Food
import time
screen = Screen()
snake = Snake()
food = Food()
sb=Scoreboard()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)
screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)


    snake.move()
    if snake.segments[0].distance(food) < 15:
        food.refresh()
        snake.extend()
        sb.increaseCount()
    if snake.segments[0].xcor() > 280 or snake.segments[0].xcor() <-280 or snake.segments[0].ycor() >280 or snake.segments[0].ycor() <-280:
        sb.game_over()
        game_is_on = False

    for segment in snake.segments[1:]:
        if snake.segments[0].distance(segment) < 10:
            sb.game_over()
            game_is_on=False

screen.exitonclick()
