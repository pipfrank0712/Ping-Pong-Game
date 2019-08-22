import turtle
import os

wn = turtle.Screen()
wn.title("Ping Pong by Frank")
wn.bgcolor("black")
wn.setup(width = 800, height=600)
wn.tracer(0)     #speed up game
wn.bgpic("buddy_background.gif")

turtle.register_shape("heart2.gif")
turtle.register_shape("left.gif")
turtle.register_shape("right.gif")

#Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)   # for max animation speed
paddle_a.shape("left.gif")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid = 5, stretch_len = 1)
paddle_a.penup()
paddle_a.goto(-350,0)

#Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)   # for max animation speed
paddle_b.shape("right.gif")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid = 5, stretch_len = 1)
paddle_b.penup()
paddle_b.goto(350,0)

#Ball
ball = turtle.Turtle()
ball.speed(0)   # for max animation speed
ball.shape("heart2.gif")
ball.color("white")
ball.penup()
ball.goto(0,0)
ball.dx = 2   	#setting diagonal move
ball.dy = 2

#move the paddles
# Move the player left and right
paddle_speed = 20

def paddle_a_up():
	y = paddle_a.ycor()  # findout paddle coordinate
	y += paddle_speed
	if y > 250:       #### boundary check
		y = 250
	paddle_a.sety(y)

def paddle_a_down():
	y = paddle_a.ycor()  # findout paddle coordinate
	y -= paddle_speed
	if y < -250:       #### boundary check
		y = -250
	paddle_a.sety(y)
def paddle_b_up():
	y = paddle_b.ycor()  # findout paddle coordinate
	y += paddle_speed
	if y > 250:       #### boundary check
		y = 250
	paddle_b.sety(y)

def paddle_b_down():
	y = paddle_b.ycor()  # findout paddle coordinate
	y -= paddle_speed
	if y < -250:       #### boundary check
		y = -250
	paddle_b.sety(y)

# Draw the score  #############################################
score1 = 0
score2 = 0
score_pen = turtle.Turtle()
score_pen.speed(0)
score_pen.color("white")
score_pen.penup()
score_pen.setposition(0,260)
scorestring = "Player1 %s  :  Player2 %s" %(score1, score2)   ###########fill in the score
score_pen.write(scorestring, False, align="center", font= ("Arial", 24, "normal"))
score_pen.hideturtle()

#keyword founding
turtle.listen()                     ##### library for binding keyboard
turtle.onkey(paddle_a_up, "w")      # lowercase w  # same effect using onkeypress
turtle.onkey(paddle_a_down, "s")    # lowercase s
turtle.onkey(paddle_b_up, "Up")
turtle.onkey(paddle_b_down, "Down")

#Main game loop
while True:
	wn.update()

	#move the ball
	ball.setx(ball.xcor() + ball.dx)
	ball.sety(ball.ycor() + ball.dy)
	
	# border check
	if ball.ycor() > 290:
		ball.sety(290)
		ball.dy *= -1
	if ball.ycor() < -290:
		ball.sety(-290)
		ball.dy *= -1
	if ball.xcor() > 390:
		ball.goto(0,0)
		ball.dx *= -1
		score1 += 1
		# scorestring = "Player1 %s  :  Player2 %s" %(score1, score2)   ###########fill in the score
		scorestring = "Player1 {}  :  Player2 {}".format(score1, score2)
		score_pen.clear()
		score_pen.write(scorestring, False, align="center", font= ("Arial", 24, "normal"))
		os.system("afplay game.wav")
	if ball.xcor() < -390:
		ball.goto(0,0)
		ball.dx *= -1
		score2 += 1
		os.system("afplay game.wav")
		# scorestring = "Player1 %s  :  Player2 %s" %(score1, score2)   ###########fill in the score
		scorestring = "Player1 {}  :  Player2 {}".format(score1, score2)		
		score_pen.clear()
		score_pen.write(scorestring, False, align="center", font= ("Arial", 24, "normal"))
		# paddle and ball collisions
	if ball.xcor() > 320  and ball.xcor()< 340 and ball.ycor() < paddle_b.ycor() + 60 and ball.ycor() > paddle_b.ycor() - 60:
		ball.setx(320)
		ball.dx *= -1	
		os.system("afplay bounce.wav &")
	if ball.xcor() < -340 and ball.xcor()> -350 and ball.ycor() < paddle_a.ycor() + 60 and ball.ycor() > paddle_a.ycor() - 60:
		ball.setx(-340)		
		ball.dx *= -1	
		os.system("afplay bounce.wav &")