#This project demonstrates a drawing using the Turtle Graphic.
#February 20, 2020
#CTI-110 P2HW2-Turtle Graphic
#Christopher Lucas

#Setup Turtle
import turtle
turtle.speed(10)
turtle.setup(700, 700)
turtle.penup()
turtle.hideturtle()

#Set coordinates and variables for seperate points
POINT_1_X = -225
POINT_1_Y = 225

POINT_2_X = 225
POINT_2_Y = 225

POINT_3_X = 0
POINT_3_Y = 0

POINT_4_X = -225
POINT_4_Y = -225

POINT_5_X = 225
POINT_5_Y = -225

#Draw dots at each point
turtle.pensize(5)
turtle.goto(POINT_1_X, POINT_1_Y)
turtle.dot()
turtle.goto(POINT_2_X, POINT_2_Y)
turtle.dot()
turtle.goto(POINT_3_X, POINT_3_Y)
turtle.dot()
turtle.goto(POINT_4_X, POINT_4_Y)
turtle.dot()
turtle.goto(POINT_5_X, POINT_5_Y)
turtle.dot()
turtle.pensize(1)

#Draw solid lines from point 1 to point 4
turtle.goto(POINT_1_X, POINT_1_Y)
turtle.pendown()
turtle.goto(POINT_4_X, POINT_4_Y)
turtle.penup()

#Draw a solid line from point 2 to point 5
turtle.goto(POINT_2_X, POINT_2_Y)
turtle.pendown()
turtle.goto(POINT_5_X, POINT_5_Y)
turtle.penup()

#Draw a solid line from point 1 to point 5
turtle.goto(POINT_1_X, POINT_1_Y)
turtle.pendown()
turtle.goto(POINT_5_X, POINT_5_Y)
turtle.penup()

#Draw a solid line from point 2 to point 4
turtle.goto(POINT_2_X, POINT_2_Y)
turtle.pendown()
turtle.goto(POINT_4_X, POINT_4_Y)
turtle.penup

#Draw a broken line from point 1 to point 2
turtle.goto(POINT_1_X, POINT_1_Y)
turtle.pendown()
turtle.forward(50)
turtle.penup()
turtle.forward(50)
turtle.pendown()
turtle.forward(100)
turtle.penup()
turtle.forward(50)
turtle.pendown()
turtle.forward(100)
turtle.penup()
turtle.forward(50)
turtle.pendown()
turtle.forward(50)
turtle.penup()

#Draw a broken line from point 4 to point 5
turtle.goto(POINT_4_X, POINT_4_Y)
turtle.pendown()
turtle.forward(50)
turtle.penup()
turtle.forward(50)
turtle.pendown()
turtle.forward(100)
turtle.penup()
turtle.forward(50)
turtle.pendown()
turtle.forward(100)
turtle.penup()
turtle.forward(50)
turtle.pendown()
turtle.forward(50)
turtle.penup()

#Program finished
turtle.done()
