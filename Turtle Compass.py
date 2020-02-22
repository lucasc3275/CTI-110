#Turtle setup
import turtle
turtle.speed(7)
turtle.hideturtle()
turtle.penup()
turtle.setup(400, 400)

#Draw a solid line indicating East and label
turtle.goto(0, 0)
turtle.pendown()
turtle.forward(100)
turtle.penup()
turtle.goto(110, -5)
turtle.write('East')

#Draw a solid line indicating North and label
turtle.goto(0, 0)
turtle.pendown()
turtle.left(90)
turtle.forward(100)
turtle.penup()
turtle.goto(-10, 105)
turtle.write('North')

#Draw a solid line indicating South and label
turtle.goto(0, 0)
turtle.pendown()
turtle.left(180)
turtle.forward (100)
turtle.penup()
turtle.goto(-10, -115)
turtle.write('South')

#draw a solid line indicating West and label
turtle.goto(0, 0)
turtle.pendown()
turtle.right(90)
turtle.forward(100)
turtle.penup()
turtle.goto(-135, -5)
turtle.write('West')

#Draw a circle at the intersect point
turtle.goto(0, 20)
turtle.pendown()
turtle.circle (20)

#Project finished
turtle.done()
