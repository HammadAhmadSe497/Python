import turtle
import math

t = turtle.Turtle()

def calculate_circle_area(radius):
  area = math.pi * radius**2
  return area

def get_input():
  center_x = float(input("Enter x-coordinate of center: "))
  center_y = float(input("Enter y-coordinate of center: "))
  radius = float(input("Enter radius of circle: "))
  return center_x, center_y, radius

center_x, center_y, radius = get_input()
t.penup()
t.goto(center_x, center_y)
t.pendown()

t.pencolor("blue")

t.circle(radius)

area = calculate_circle_area(radius)
t.penup()
t.goto(center_x, center_y + radius)
t.pendown()

t.write(f"Area: {area:.2f}", align="center", font=("Arial", 12, "normal"))

turtle.done()
