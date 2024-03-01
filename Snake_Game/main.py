import Snake as s
from turtle import Screen
from scoreBoard import ScoreBoard
import time
from food import Food

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
SCREEN_UTMOST_RIGHT = SCREEN_WIDTH / 2
SCREEN_UTMOST_LEFT = -(SCREEN_WIDTH / 2)
SCREEN_UTMOST_TOP = SCREEN_HEIGHT / 2
SCREEN_UTMOST_BOTTOM = -(SCREEN_HEIGHT / 2)


screen = Screen()
screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
screen.tracer(0)
snake_ = s.Snake()   
screen.listen()
screen.onkey(snake_.up, "Up")
screen.onkey(snake_.down, "Down")
screen.onkey(snake_.left, "Left")
screen.onkey(snake_.right, "Right")

score = ScoreBoard()
food = Food()

# To move snake forward
game_is_on = True
while game_is_on:
    screen.update()
    if snake_.snake_list.__len__()>5:
        time.sleep(0.1)
    elif snake_.snake_list.__len__()>8:
        time.sleep(0)
    else:
        time.sleep(0.2)
    snake_.move()
    # Detect collision with food - If the distance between 2 turtles is less than 15
    if snake_.head.distance(food) < 15:
        food.newLocation()
        score.increase_score()
        snake_.extend()  

    # detect collision with wall
    if (
        snake_.head.xcor() > (SCREEN_UTMOST_RIGHT - 10)
        or snake_.head.xcor() < (SCREEN_UTMOST_LEFT + 10)
        or snake_.head.ycor() > (SCREEN_UTMOST_TOP - 10)
        or snake_.head.ycor() < (SCREEN_UTMOST_BOTTOM + 10)
    ):
        score.reset()

    # detect collision with the tail snake
    # if head collides with any segment then game over
    for segment in snake_.snake_list:
        if snake_.head.distance(segment) < 10 and segment != snake_.head:
            score.reset()

screen.exitonclick()
