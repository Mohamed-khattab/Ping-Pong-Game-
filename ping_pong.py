
import turtle
import time

player_one =input("please enter the player one name : ")       # to print an empty line 
player_two =input("please enter the player two name : ")      # to print an empty line 
complex =  input("please choose the Game mode easy or middle or hard  :")  # the level of ball speed


wind = turtle.Screen()             # screen initialization 
wind.title("Ping pong game ")      # window title  
wind.bgcolor("green")             # set the background color 
wind.setup(width=900, height=700)   # set the width and the hieght of the window 
wind.tracer(0)                     # stop the window from updating automatically 

#racquet_one
racquet_one = turtle.Turtle()  # initialize object 
racquet_one.speed(0)           # set the speed of animation 
racquet_one.shape("square")    # set the shape of racquet one 
racquet_one.color("blue")      # set the color of racquet one 
racquet_one.shapesize(stretch_wid=5, stretch_len=1)   # stretch the size
racquet_one.penup()  # stop drawing lines 
racquet_one.goto(-420, 0)  # set the position for racquet one 

#racquet_two

racquet_two = turtle.Turtle()   # initialize object 
racquet_two.speed(0)            # set the speed of animation 
racquet_two.shape("square")     # set the shape of racquet two 
racquet_two.color("red")        # set the color  of racquet two 
racquet_two.shapesize(stretch_wid=5, stretch_len=1)  # stretch the size
racquet_two.penup()
racquet_two.goto(420, 0)         # set the position for racquet one 

#ball

ball = turtle.Turtle()   
ball.speed(0)
ball.shape("circle")
ball.color("yellow")
ball.penup()
ball.goto(0, 0)

if (complex == 'easy'):  # complexity level check 
   ball.dx = 0.3
   ball.dy = 0.3 
elif (complex == 'middle'):
  ball.dx = 0.8
  ball.dy = 0.8 
elif(complex =='hard') :
  ball.dx = 1.1
  ball.dy = 1.1 

def speed_up() :   # to increase the velocity oa the ball if one of the players won the other a match out of 10
   ball.dx += 0.1
   ball.dy += 0.1


#score
score1 = 0
score2 = 0
score = turtle.Turtle()
score.speed(0)
score.color("white")
score.penup()
score.hideturtle()
score.goto(0, 260)
score.write("Player 1: 0 player 2: 0", align="center", font=("Courier",24,"normal"))

#functions to move two racquets 

def racquet_one_up():
    y = racquet_one.ycor()    #  get the y coredinates of racquey one 
    y += 60               #set the y cordintes to increase by 20
    racquet_one.sety(y)

def racquet_one_down():
    y = racquet_one.ycor()
    y -= 60              #set the y cordintes to decrease by 20
    racquet_one.sety(y)

def racquet_two_up():
    y = racquet_two.ycor()
    y += 60                 ##set the y cordintes to increase by 20
    racquet_two.sety(y)

def racquet_two_down():
    y = racquet_two.ycor()
    y -= 60                #set the y cordintes to decrease by 20
    racquet_two.sety(y)

#keyboard bindings
wind.listen()            # tell the window to excpect the input 
wind.onkeypress(racquet_one_up, "w") 
wind.onkeypress(racquet_one_down, "s")

wind.onkeypress(racquet_two_up, "Up")
wind.onkeypress(racquet_two_down, "Down")

#game loop

while True:
    wind.update()

    # move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

     # border check
    if ball.ycor() >340:         # note : the ball radious is 20 pixcel so 340 means it exceded the racquet
        ball.sety(340)
        ball.dy *= -1

    if ball.ycor() <-340:
        ball.sety(-340)
        ball.dy *= -1

    if ball.xcor() >440:
        ball.goto(0, 0)
        ball.dx *= -1
        score1+= 1
        score.clear()
        score.write("{}'s score : {} | {}'s score  : {}".format( player_one ,score1,player_two, score2), align="center", font=("Courier", 20, "normal"))
   
    if((score1 > score2 )and(score1  >= 10 )):
           score.clear()
           score.write("Congratulation for {} , you win ".format( player_one ), align="center", font=("Courier", 20, "normal"))
           time.sleep(1)
           score1 , score2 = 0,0
           speed_up()

    if ball.xcor() <-440:
        ball.goto(0, 0)
        ball.dx *= -1
        score2 += 1
        score.clear()
        score.write("{}'s score : {} | {}'s score  : {}".format( player_one ,score1,player_two, score2), align="center", font=("Courier", 20, "normal"))
   
    if((score2 > score1 )and(score2  >= 10 )):
           score.clear()
           score.write("Congratulation for {} , you win ".format( player_two ), align="center", font=("Courier", 20, "normal"))
           time.sleep(1)
           score1 ,score2 = 0,0 
           speed_up()

    # racquet and ball collision

    if (ball.xcor() > 410 and ball.xcor() <420) and (ball.ycor() < racquet_two.ycor() + 40 and ball.ycor() > racquet_two.ycor() -40):
        ball.setx(410)
        ball.dx *= -1
    
    if (ball.xcor() < -410 and ball.xcor() > -420) and (ball.ycor() < racquet_one.ycor() + 40 and ball.ycor() > racquet_one.ycor() -40):
        ball.setx(-410)
        ball.dx *= -1