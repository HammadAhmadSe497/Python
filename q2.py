import turtle
turtle.pensize(3)
turtle.color("red")
#triangle
turtle.penup()
turtle.goto(-200,-50)
turtle.pendown()
turtle.circle(40, steps = 3)
#Rectangle
turtle.penup()
turtle.goto(-100,-50)
turtle.pendown()
turtle.circle(40, steps = 4)
#Pentagon
turtle.penup()
turtle.goto(0,-50)
turtle.pendown()
turtle.circle(40, steps = 5)
#octagon
turtle.penup()
turtle.goto(100,-50)
turtle.begin_fill()
turtle.color("blue")
turtle.pendown()
turtle.circle(40, steps = 8)
turtle.end_fill()