#Orions Belt Turtle Practice
import turtle

turtle.setup(500, 600)
turtle.penup()
turtle.hideturtle()

#set coordinates and variables for stars
LEFT_SHOULDER_X = -70
LEFT_SHOULDER_Y = 200

RIGHT_SHOULDER_X = 80
RIGHT_SHOULDER_Y = 180

LEFT_BELTSTAR_X = -40
LEFT_BELTSTAR_Y = -20

MIDDLE_BELTSTAR_X = 0
MIDDLE_BELTSTAR_Y = 0

RIGHT_BELTSTAR_X = 40
RIGHT_BELTSTAR_Y = 20

LEFT_KNEE_X = -90
LEFT_KNEE_Y = -180

RIGHT_KNEE_X = 120
RIGHT_KNEE_Y = -140

#Draw Stars
turtle.goto(LEFT_SHOULDER_X, LEFT_SHOULDER_Y)
turtle.dot()
turtle.goto(RIGHT_SHOULDER_X, RIGHT_SHOULDER_Y)
turtle.dot()
turtle.goto(LEFT_BELTSTAR_X, LEFT_BELTSTAR_Y)
turtle.dot()
turtle.goto(MIDDLE_BELTSTAR_X, MIDDLE_BELTSTAR_Y)
turtle.dot()
turtle.goto(RIGHT_BELTSTAR_X, RIGHT_BELTSTAR_Y)
turtle.dot()
turtle.goto(LEFT_KNEE_X, LEFT_KNEE_Y)
turtle.dot()
turtle.goto(RIGHT_KNEE_X, RIGHT_KNEE_Y)
turtle.dot()

#Name Stars
turtle.goto(LEFT_SHOULDER_X, LEFT_SHOULDER_Y)
turtle.write('Betelguese')
turtle.goto(RIGHT_SHOULDER_X, RIGHT_SHOULDER_Y)
turtle.write('Meissa')
turtle.goto(LEFT_BELTSTAR_X, LEFT_BELTSTAR_Y)
turtle.write('Alnitak')
turtle.goto(MIDDLE_BELTSTAR_X, MIDDLE_BELTSTAR_Y)
turtle.write('Alnilam')
turtle.goto(RIGHT_BELTSTAR_X, RIGHT_BELTSTAR_Y)
turtle.write('Mintaka')
turtle.goto(LEFT_KNEE_X, LEFT_KNEE_Y)
turtle.write('Saiph')
turtle.goto(RIGHT_KNEE_X, RIGHT_KNEE_Y)
turtle.write('Rigel')

#Draw a line from left shoulder to left belt star
turtle.goto(LEFT_SHOULDER_X, LEFT_SHOULDER_Y)
turtle.pendown()
turtle.goto(LEFT_BELTSTAR_X, LEFT_BELTSTAR_Y)
turtle.penup()

#Draw a line from right shoulder to right belt star
turtle.goto(RIGHT_SHOULDER_X, RIGHT_SHOULDER_Y)
turtle.pendown()
turtle.goto(RIGHT_BELTSTAR_X, RIGHT_BELTSTAR_Y)
turtle.penup()

#Draw a line from middle belt star to right belt star
turtle.goto(MIDDLE_BELTSTAR_X, MIDDLE_BELTSTAR_Y)
turtle.pendown()
turtle.goto(RIGHT_BELTSTAR_X, RIGHT_BELTSTAR_Y)
turtle.penup()

#Draw a line from left belt star to middle beltstar
turtle.goto(LEFT_BELTSTAR_X, LEFT_BELTSTAR_Y)
turtle.pendown()
turtle.goto(MIDDLE_BELTSTAR_X, MIDDLE_BELTSTAR_Y)
turtle.penup()

#Draw a line from left belt star to left knee
turtle.goto(LEFT_BELTSTAR_X, LEFT_BELTSTAR_Y)
turtle.pendown()
turtle.goto(LEFT_KNEE_X, LEFT_KNEE_Y)
turtle.penup()

#Draw a line from right belt star to right knee
turtle.goto(RIGHT_BELTSTAR_X, RIGHT_BELTSTAR_Y)
turtle.pendown()
turtle.goto(RIGHT_KNEE_X, RIGHT_KNEE_Y)
turtle.penup()

turtle.done()
