### TURTLE.py ###
#-----Set 1-----#
#===10/29/25====#
#################

import turtle
 
NUM_CIRCLES = 20
STARTING_RADIUS = 20
OFFSET = 10
ANIMATION_SPEED = 0

turtle.speed(ANIMATION_SPEED)
turtle.hideturtle()

radius = STARTING_RADIUS

for count in range(NUM_CIRCLES):

    turtle.circle(radius)

    x = turtle.xcor()
    y = turtle.ycor() - OFFSET

    radius = radius + OFFSET

    turtle.penup()
    turtle.goto(x,y)
    turtle.pendown()
