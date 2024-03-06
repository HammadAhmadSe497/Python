import turtle

# Function to draw a shape with specified n of sides, filled or not
def draw_shape(sides, filled, pen_size=3):
  t.pensize(pen_size)  # Set pen size
  angle = 180 - (180 * (sides - 2)) / sides  # Calculate interior angle
  if filled:
    t.begin_fill()  # Start filling for filled shapes
  for _ in range(sides):
    t.forward(100)  # Adjust length as needed
    t.left(angle)
  if filled:
    t.end_fill()  # End filling

# Create turtle object
t = turtle.Turtle()

# Move turtle to the left edge (adjust as needed)
t.penup()
t.goto(-350, 0)  # Adjust x-coordinate for left alignment
t.pendown()

# Draw shapes (filled and not filled)
draw_shape(3, False)  # Triangle (not filled)
t.penup()
t.forward(150)  # Move turtle right for next shape
t.pendown()
draw_shape(3, True)  # Triangle (filled)

t.penup()
t.forward(150)  # Move turtle right for next shape
t.pendown()
draw_shape(4, False)  # Square (not filled)

t.penup()
t.forward(150)  # Move turtle right for next shape
t.pendown()
draw_shape(4, True)  # Square (filled)

t.penup()
t.forward(150)  # Move turtle right for next shape
t.pendown()
draw_shape(6, False)  # Hexagon (not filled)

t.penup()
t.forward(150)  # Move turtle right for next shape
t.pendown()
draw_shape(6, True)  # Hexagon (filled)

t.penup()
t.forward(150)  # Move turtle right for next shape
t.pendown()
draw_shape(8, False)  # Octagon (not filled)

t.penup()
t.forward(150)  # Move turtle right for next shape
t.pendown()
draw_shape(8, True)  # Octagon (filled)

# Keep the window open
turtle.done()
