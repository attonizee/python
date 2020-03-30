#!/bin/python3

import turtle
import random
import math

phi = 360 / 7
r = 50

def gotoxy(x,y):
    turtle.penup()
    turtle.goto(x,y)
    turtle.pendown()

def draw_circle(r,color):
    turtle.fillcolor(color)
    turtle.begin_fill()
    turtle.circle(r)
    turtle.end_fill()

def baraban(x,y):
    gotoxy(x,y)
    turtle.circle(80)
    gotoxy(x, y + 160)
    draw_circle(5, 'red')
    for i in range(0,7):
            phi_rad = phi * i * math.pi / 180.0
            gotoxy(x + math.sin(phi_rad) * r, y + math.cos(phi_rad) * r + 60)
            draw_circle(22, 'white')

def baraban_anim(x,y,start):
    for i in range(start,random.randrange(7,34)):
            phi_rad = phi * i * math.pi / 180.0
            gotoxy(x + math.sin(phi_rad) * r, x + math.cos(phi_rad) * r + 60)
            draw_circle(22, 'brown')
            draw_circle(22, 'white')
    gotoxy(x + math.sin(phi_rad) * r, x + math.cos(phi_rad) * r + 60)
    draw_circle(22, 'brown')
    return i % 7
    


turtle.speed(0)


baraban(100,100)

answer = ''
start = 0
while answer != 'N':
    answer = turtle.textinput("Let's play?", "Y/N")

    if answer == 'Y':
       start = baraban_anim(100, 100, start)
       if start % 7 == 0:
           gotoxy(-150, 250)
           turtle.write("You loose", font=("Arial", 18, "normal"))
    else:
        pass