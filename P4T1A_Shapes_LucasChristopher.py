#CTI-110
#P4T1A-Shapes
#Christopher Lucas
#March 20, 2020

#import turtle
#set forward range and assign variable "forward_range"
#set starting X & Y coordinates and assign variables "start_x & start_y"
#penup and goto starting coordinates
#setheading to 180
#pendown and set speed to 0
#for x in range 100
#draw square using "forward_range" and 90 degree right turns
#at the end of each square add 5 to "forward_range"

import turtle

forward_range=20
start_x=250
start_y=-250

turtle.hideturtle()
turtle.penup()
turtle.goto(start_x, start_y)
turtle.setheading(180)
turtle.pendown()
turtle.speed(0)
for x in range(100):
    turtle.forward(forward_range)
    turtle.right(90)
    turtle.forward(forward_range)
    turtle.right(90)
    turtle.forward(forward_range)
    turtle.right(90)
    turtle.forward(forward_range)
    turtle.right(90)
    forward_range+=5
    