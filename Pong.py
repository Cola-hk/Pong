import turtle
import random
import sys
import winsound
import time

#Game state
game_state = "splash"

#Window
wn = turtle.Screen()
wn.title("Pong by @Cola")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

#start screen
start_txt = turtle.Turtle()
start_txt.speed(0)
start_txt.goto(0,40)
start_txt.hideturtle()
start_txt.color("white")
start_txt.write("Press x to start" ,align="center" , font=("impact", 35, "bold"))

#Score
score_a = 0
score_b = 0

#setting - defult
inputspeed = 10
speed = 0.1


#Paddle A
paddle_a = turtle.Turtle()
paddle_a.st()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5 ,stretch_len = 1)
paddle_a.penup()
paddle_a.goto(-350,0)

#Paddle B
paddle_b = turtle.Turtle()
paddle_b.st()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5 ,stretch_len = 1)
paddle_b.penup()
paddle_b.goto(+350,0)

#Pause
pause_txt = turtle.Turtle()
pause_txt.speed(0)
pause_txt.penup()
pause_txt.hideturtle()
pause_txt.goto(0,40)


#Ball
ball = turtle.Turtle()
ball.st()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0,0)
ball.dx = random.choice([speed ,-speed])
ball.dy = random.choice([speed ,-speed])

#Pen
score = turtle.Turtle()
score.speed(0)
score.color("white")
score.penup()
score.hideturtle()
score.goto(0,240)
score.write("0  0" ,align="center" , font=  ("impact", 35, "normal"))

padspeed = 20

#Function
def setting_ball():
    global inputspeed
    inputspeed = turtle.textinput("Speed of ball", "How fast ?") 

def setting_pad():
    global padspeed
    padspeed = turtle.textinput("Speed of paddle", "How fast ?")

def paddle_a_up():
    y = paddle_a.ycor()
    y += padspeed
    paddle_a.sety(y)
    

def paddle_a_down():
    y = paddle_a.ycor()
    y -= padspeed
    paddle_a.sety(y)


def paddle_b_up():
    y = paddle_b.ycor()
    y += padspeed
    paddle_b.sety(y)


def paddle_b_down():
    y = paddle_b.ycor()
    y -= padspeed
    paddle_b.sety(y)


def exitprogram():
    wn.bye()

def paused():
    global game_state
    game_state = "paused"

    pause_txt.color("white")
    pause_txt.write("Press Enter to confirm quit\nPress B to change ball speed\nPress P to change paddle speed\nPress X to resume" ,align="center" , font=("impact", 24, "normal"))


    start_txt.clear()


def start_game():
    global game_state
    game_state = "running"
    pause_txt.clear()



#Keyboard binding
wn.listen()
wn.onkeypress(paddle_a_up,"w")
wn.onkeypress(paddle_a_up,"W")
wn.onkeypress(paddle_a_down,"s")
wn.onkeypress(paddle_a_down,"S")
wn.onkeypress(paddle_b_up,"Up")
wn.onkeypress(paddle_b_down,"Down")
wn.onkeypress(paused,"Escape")
wn.onkeypress(paused,"Escape")



#game loop
while True:
    wn.update()

    inputspeed = float(inputspeed)
    speed = inputspeed / 100

    padspeed = float(padspeed)


    if game_state == "splash":
        wn.listen()
        wn.onkeypress(start_game,"x")
        wn.onkeypress(start_game,"X")


    if game_state == "paused":
        wn.listen()
        wn.onkeypress(exitprogram, "Return")
        wn.onkeypress(start_game,"x")
        wn.onkeypress(start_game,"X")
        wn.onkeypress(setting_pad,"p")
        wn.onkeypress(setting_ball,"b")
        ball.ht()

    if game_state == "running":

        ball.setx(ball.xcor() + ball.dx)
        ball.sety(ball.ycor() + ball.dy)

        start_txt.penup()
        start_txt.clear()
        ball.st()

    #paddle boarder
    if paddle_a.ycor() > 260:
        y = paddle_a.ycor()
        y -=20
        paddle_a.sety(y)


    if paddle_a.ycor() < -260:
        y = paddle_a.ycor()
        y +=20
        paddle_a.sety(y)

    if paddle_b.ycor() > 260:
        y = paddle_b.ycor()
        y -=20
        paddle_b.sety(y)


    if paddle_b.ycor() < -260:
        y = paddle_b.ycor()
        y +=20
        paddle_b.sety(y)


    #border
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
        winsound.PlaySound("boom.wav", winsound.SND_ASYNC)

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
        winsound.PlaySound("boom.wav", winsound.SND_ASYNC)

    if ball.xcor() > 390 and game_state == "running":
        ball.goto(0,0)
        ball.dy = random.choice([speed ,- speed])
        ball.dx = random.choice([speed ,- speed])
        score_a += 1
        score.clear()
        score.write("{}  {}".format(score_a, score_b) ,align="center" , font=("Squada One", 35, "bold"))


    if ball.xcor() < -390and game_state == "running":
        ball.goto(0,0)
        ball.dy = random.choice([speed ,- speed])
        ball.dx = random.choice([speed ,- speed])
        score_b  += 1
        score.clear()
        score.write("{}  {}".format(score_a, score_b) ,align="center" , font=("Squada One", 35, "bold"))


    #collisions
    if (ball.xcor() < -340 and ball.xcor() > -350 ) and (ball.ycor() < paddle_a.ycor() + 40 and ball.ycor() > paddle_a.ycor() -50):
        ball.setx(-340)
        ball.dx *= -1
        winsound.PlaySound("boom.wav", winsound.SND_ASYNC)


    if (ball.xcor() > 340 and ball.xcor() >350) and (ball.ycor() < paddle_b.ycor() + 40 and ball.ycor() > paddle_b.ycor() - 50):
        ball.setx(340)
        ball.dx *= -1
        winsound.PlaySound("boom.wav", winsound.SND_ASYNC)

#Speed - input and increase
#Soundtrack
#Colour settingl