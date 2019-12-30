#simplistic pong game made with turtle module

#the modules necessary
import turtle
from os import*
import random


#To spice up the game
# Direction_Gen = [-1,1]
#variable for convention
screen_size_w= 800
screen_size_h = 800
#screen setup
wn = turtle.Screen()
wn.title("Pong by @san.mamba")
wn.bgcolor("black")
#wn.bgpic("uchiha.png")#not running in VS code but perfect in notepadd++
wn.setup(width= screen_size_w, height= screen_size_h)
wn.tracer(0)

#middle screen separator ON DEVELOPMENT
# separator = turtle.Turtle()
# separator.shape("square")
# separator.color("white")
# separator.shapesize(stretch_wid = 50, stretch_len=-2)

#paddle 1
paddle_1 = turtle.Turtle()
paddle_1.speed(0)
paddle_1.shape("square")
paddle_1.color("blue")
paddle_1.penup()
paddle_1.goto(screen_size_w/-2 + 40, 0)
paddle_1.shapesize(stretch_wid=5,stretch_len=1)


#paddle 2
paddle_2 = turtle.Turtle()
paddle_2.speed(0)
paddle_2.shape("square")
paddle_2.color("red")
paddle_2.penup()
paddle_2.goto(screen_size_w/2 - 40, 0)
paddle_2.shapesize(stretch_wid=5,stretch_len=1)

#ball
ball=turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("yellow")
ball.penup()
ball.goto(0,0)
ball.shapesize(stretch_wid=1.3)

#ball movement
ball.dx = 1
ball.dy = 1

#fonctions for movement
#for paddle 1
def paddle_1_up() :#up
    y = paddle_1.ycor()
    y = y+20
    paddle_1.sety(y)
def paddle_1_down() :#down
    y = paddle_1.ycor()
    y = y-20
    paddle_1.sety(y)

#for paddle 2
def paddle_2_up():
    y=paddle_2.ycor()
    y=y+20
    paddle_2.sety(y)
def paddle_2_down():
    y=paddle_2.ycor()
    y=y-20
    paddle_2.sety(y)
#key binding
wn.listen()
wn.onkeypress(paddle_1_up,"z")
wn.onkeypress(paddle_1_down,"s")
wn.onkeypress(paddle_2_up,"Up")
wn.onkeypress(paddle_2_down,"Down")
#main game loop
while True:
    # Dir_geny = random.choice(Direction_Gen)
    wn.update()
    

    #ball movement loop
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    #Generating bouncing borders
    #upper border
    if ball.ycor() >  390 :
        ball.sety( 390)
        ball.dy *= -1
    #lower border
    if ball.ycor() <  -380 :
        ball.sety( -380)
        ball.dy *= -1

    #if the ball scores then reappears in the middle and changes direction
    if ball.xcor() > 390:
        ball.setx(0)
        ball.dx = ball.dx * -1
        # ball.dy =Dir_geny
    if ball.xcor() < -390:
        ball.setx(0)
        ball.dx = ball.dx * -1
        # ball.dy =Dir_geny
    

    #ball bounce conditions
    if (ball.xcor() > 340 and ball.xcor() < 350 ) and (ball.ycor() < paddle_2.ycor() + 50 and ball.ycor() > paddle_2.ycor() - 50) :
        ball.dx = ball.dx * -1
    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_1.ycor() + 50 and ball.ycor() > paddle_1.ycor() - 50) :
        ball.dx = ball.dx * -1