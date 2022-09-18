
from os import system as sys
from turtle import *
import turtle as tr
import time
import random as rnd

def go_up():
    head.setheading(90)

def go_down():
    head.setheading(270)
def go_right():
    head.setheading(0)

def go_left():
    head.setheading(180)

def popup_food():
    food.goto(rnd.randint(-320,320), rnd.randint(-273,273))
    foodpos[0]=food.xcor()
    foodpos[1]=food.ycor()
    print(foodpos[0],foodpos[1])
    food.showturtle()

def add_score(count):
    count=0
    score.write("Score:", count)
def check():
    headpos[0]=head.xcor()
    headpos[1]=head.ycor()
    if headpos[0]>=foodpos[0]-15 and headpos[0]<=foodpos[0]+15:
        if headpos[1]>=foodpos[1]-13 and headpos[1]<=foodpos[1]+17:
            popup_food()
            add_score()

def main(x,y):
    head.hideturtle()
    time.sleep(0.2)
    head.showturtle()
    while True:
        listen()
        onkey(go_up,"Up")
        onkey(go_down,"Down")
        onkey(go_left,"Left")
        onkey(go_right,"Right")
        head.forward(15)
        check()
def pause():
    head.goto(head.xcor(),head.ycor())





tr.bgpic('C:\\Users\\amzan\\Documents\\Projets py\\Snake\\Gwa0f8Z.png')
tr.title('snake')
tr.screensize(789,547)
tr.hideturtle()
begin_fill()
score=tr.Turtle()
score.hideturtle()
score.pu()
score.goto(-250,250)
head = tr.Turtle()
food=tr.Turtle()
headpos=[0,0]
foodpos=[0,0]
head.color("black")
head.shape("square")
head.pu()
head.speed(2)
food.hideturtle()
food.speed(0)
food.pu()
food.color("yellow")
food.shape("square")
food.penup()
food.hideturtle()
food.shapesize(0.8, 0.8)

sys("cls")

listen()
onscreenclick(main,1)
popup_food()

food.showturtle()
end_fill()

mainloop()

"""
if position of the food (135,13)
the head can eat till y: -4 to 30
x: 116 to 153
135-19 and 135+18
9-13 and 13+17
"""
