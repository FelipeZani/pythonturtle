from os import system as sys
from turtle import *
import turtle as tr
wn=tr.Screen()
wn.title('snake')

wn.bgpic('C:\\Users\\amzan\\Documents\\Projets py\\Snake\\Gwa0f8Z.png')
def snake():
    color('black', 'black')
    begin_fill()
    for i in range(4):
        forward(25)
        left(90)
    end_fill()

def snake_forward():
    a=0
    while True:
        snake()
        penup()
        goto(a,0)
        a+=10
        pendown()


snake_forward()
done()
