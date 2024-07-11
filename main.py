from turtle import Screen
from Paddle import Paddle
from Ball import Ball
import time
from scoreboard import Scoreboard

screen = Screen()
ball = Ball()
scoreboard = Scoreboard()

screen.setup(height=600,width=800)
screen.bgcolor("black")
screen.title("Pong Game")
screen.listen()
screen.tracer(0)
screen.delay(0)

r_paddle = Paddle((350,0))
l_paddle = Paddle((-350,0))

screen.listen()
screen.onkey(r_paddle.up, key="Up")
screen.onkey(r_paddle.down, key="Down")
screen.onkey(l_paddle.up, key="w")
screen.onkey(l_paddle.down, key="s")


is_game_on = True
while is_game_on:
    time.sleep(0.05)
    screen.update()
    ball.move()
    #Collison with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    #Collision with paddle
    if ball.xcor() > 320 and ball.distance(r_paddle) < 50 or ball.xcor() < -320 and ball.distance(l_paddle) < 50:
        ball.bounce_x()


    #when right paddle misses ball:
    if ball.xcor() > 400 :
        ball.reset_position()
        scoreboard.l_point()

    #when left paddle missed ball:
    if ball.xcor() < -400:
        ball.reset_position()
        scoreboard.r_point()

screen.exitonclick()

