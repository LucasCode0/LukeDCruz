import turtle
import time

# Window Setup

window = turtle.Screen()
window.title('Pong')
window.bgcolor('Black')
window.setup(width = 800, height = 600)
window.tracer(0)

# Left Paddle

paddle_left = turtle.Turtle()
paddle_left.speed(0)
paddle_left.shape('square')
paddle_left.shapesize(stretch_wid = 5, stretch_len = 1)
paddle_left.color('white')
paddle_left.penup()
paddle_left.goto(-350, 0)
paddle_left_score = 0

# Right Paddle

paddle_right = turtle.Turtle()
paddle_right.speed(0)
paddle_right.shape('square')
paddle_right.shapesize(stretch_wid = 5, stretch_len = 1)
paddle_right.color('white')
paddle_right.penup()
paddle_right.goto(350, 0)
paddle_right_score = 0

# Scoreboard

scoreboard = turtle.Turtle()
scoreboard.speed(0)
scoreboard.color('white')
scoreboard.penup()
scoreboard.hideturtle()
scoreboard.goto(0, 190)
scoreboard.write(f'{paddle_left_score} : {paddle_right_score}', align = 'center', font = ('Times New Roman', 80))

# Ball

ball = turtle.Turtle()
ball.speed(0)
ball.shape('square')
ball.color('white')
ball.penup()
ball.goto(0, 0)
ball.speedX = 0.15
ball.speedY = 0.15

# Left paddle move functions

def paddle_left_up():
    y = paddle_left.ycor()
    y += 20
    paddle_left.sety(y)

def paddle_left_down():
    y = paddle_left.ycor()
    y -= 20
    paddle_left.sety(y)


# Right paddle move functions

def paddle_right_up():
    y = paddle_right.ycor()
    y += 30
    paddle_right.sety(y)

def paddle_right_down():
    y = paddle_right.ycor()
    y -= 30
    paddle_right.sety(y)

# Keyboard Binds

window.onkeypress(paddle_left_up, 'w')
window.onkeypress(paddle_left_down, 's')

window.onkeypress(paddle_right_up, 'Up')
window.onkeypress(paddle_right_down, 'Down')

# Tell computer to listen for keyboard input

window.listen()

while True:
    window.update()
    ball.setx(ball.xcor() + ball.speedX)
    ball.sety(ball.ycor() + ball.speedY)

    # Border checking
    if ball.ycor() > 300:
        ball.sety(300)
        ball.speedY *= -1

    if ball.ycor() < -300:
        ball.sety(-300)
        ball.speedY *= -1

    # Goal checking

    # Left Goal

    if ball.xcor() > 405:
        ball.goto(0, 0)
        paddle_right.goto(350, 0)
        paddle_left.goto(-350, 0)
        time.sleep(1)
        paddle_left_score += 1
        ball.speedX *= 1
        scoreboard.clear()
        scoreboard.write(f'{paddle_left_score} : {paddle_right_score}', align = 'center', font = ('Times New Roman', 80))

    # Right Goal

    if ball.xcor() < -405:
        ball.goto(0, 0)
        paddle_left.goto(-350, 0)
        paddle_right.goto(350, 0)
        time.sleep(1)
        paddle_right_score += 1
        ball.speedX *= 1
        scoreboard.clear()
        scoreboard.write(f'{paddle_left_score} : {paddle_right_score}', align = 'center', font = ('Times New Roman', 80))

    # Paddle & Ball collisions

    if (ball.xcor() < -350) and (paddle_left.ycor() -50 < ball.ycor() < paddle_left.ycor() + 50):
      ball.speedX *= -1

    if (ball.xcor() > 350) and (paddle_right.ycor() - 50 < ball.ycor() < paddle_right.ycor() + 50):
      ball.speedX *= -1


    # Paddle Bounds

    if paddle_left.ycor() > 250:
      paddle_left.sety(250)

    if paddle_right.ycor() > 250:
      paddle_right.sety(250)

    if paddle_left.ycor() < -250:
      paddle_left.sety(-250)

    if paddle_right.ycor() < -250:
      paddle_right.sety(-250)
