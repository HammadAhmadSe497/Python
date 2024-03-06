import turtle

t = turtle.Turtle()
gap = 50


def draw_polygon(num_sides, side_length):
  angle = 180 - (num_sides - 2) * 180 / num_sides
  for _ in range(num_sides):
    t.forward(side_length)
    t.left(angle)

# Rectangle
t.penup()
t.goto(-(100 + gap), 0)
t.pendown()
draw_polygon(4, 100)

# Triangle
t.penup()
t.forward(100 + gap)
t.pendown()
draw_polygon(3, 100)

# Pentagon
t.penup()
t.forward(100 + gap)
t.pendown()
draw_polygon(5, 50)

t.hideturtle()
turtle.done()
