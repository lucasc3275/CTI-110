#CTI-110
#P4T1B-Initials
#Christopher Lucas
#March 20, 2020

#import turtle
#set pen size and color
#set background color
#pen up and goto coordinates X=-50 & Y=70
#pen down & set heading to 135 degrees
#for x in range 10
#forward 50 with 30 degree left turns
#pen up & goto coordinates X=50 & Y=105
#pen down & set heading to 270 degrees
#forward 165, 90 degree left turn, forward 115

import turtle

turtle.pensize(5)
turtle.pencolor('yellow')
turtle.bgcolor('darkblue')
turtle.hideturtle()
turtle.penup()
turtle.goto(-50, 70)
turtle.pendown()
turtle.setheading(135)

for x in range(10):
    turtle.forward(50)
    turtle.left(30)
    
turtle.penup()
turtle.goto(50, 105)
turtle.pendown()
turtle.setheading(270)

turtle.forward(165)
turtle.left(90)
turtle.forward(115)

