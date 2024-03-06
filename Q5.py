import turtle

t = turtle.Turtle()

t.pensize(3)
t.pencolor("green")

def getData():
  x = float(input("Enter x-coordinate: "))
  y = float(input("Enter y-coordinate: "))
  return x, y


p1 = getData()
p2 = getData()

t.goto(p1)
t.pendown()

t.speed(0)

t.goto(p2)

distance = t.distance(p2)
print("Distance between points:", distance)

turtle.done()
