
from os import system as sys
from turtle import *
import turtle as tr
import time


wn=tr.Screen()
tr.screensize(789,547)
wn.bgpic('C:\\Users\\amzan\\Documents\\Projets py\\Snake\\Gwa0f8Z.png')
wn.title('snake')
speed(0)
#tr.hideturtle()


def snake(direction):
    color("", "red")
    begin_fill()
    for j in range(4):
        forward(25)
        if direction==1:
            left(90)
        else:
            right(90)
    end_fill()
def snake_forward():
    snake(2)
def to_up():
    snake(2)
    setheading(90)
    forward(25)
    setheading(0)
    snake(2)
def to_down():
    snake(2)
    setheading(270)
    forward(25)
    setheading(0)
    snake(2)
def to_right():
    snake(2)
    setheading(0)
    forward(25)
    setheading(0)
    snake(2)
def to_left():
    setheading(180)
    snake(1)
    forward(25)
    setheading(0)


def main (x,y):
    snake(2)
    while True:
        listen()
        onkey(to_up,"Up")
        onkey(to_down,"Down")
        onkey(to_left,"Left")
        onkey(to_right,"Right")
        snake_forward()

sys("cls")
listen()
start = 0
onscreenclick(main,1)
mainloop()
