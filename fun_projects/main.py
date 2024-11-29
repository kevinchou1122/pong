import time
from turtle import Turtle,Screen
from paddle import Paddle
from paddle2 import Paddle2
from ball import Ball
import time
from score_board import Score_board
screen=Screen()
screen.setup(800,600)
screen.bgcolor("black")
screen.title("Pong")
paddle=Paddle()
paddle2=Paddle2()
ball=Ball()
screen.listen()
score_board=Score_board()
screen.onkey(paddle2.up,"Up")
screen.onkey(paddle2.down,"Down")
screen.onkey(paddle.up,"w")
screen.onkey(paddle.down,"s")
game_on=True
while game_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    if ball.ycor()>=280 or ball.ycor()<=-280:
        ball.bounce()

    if ball.distance(paddle2)<50 and ball.xcor()>320 or ball.distance(paddle)<50 and ball.xcor()<-320 :
        print("MADE CONTACT")
        ball.bounce_x()

    if ball.xcor()<-390 or ball.xcor()>390:
        ball.speed("fastest")
        ball.goto(0,0)
        ball.direction*=-1

    if ball.xcor() < -380:
        score_board.add_r()

    if ball.xcor() > 380:
        score_board.add_l()








screen.exitonclick()