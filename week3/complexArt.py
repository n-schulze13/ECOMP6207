import turtle
import random

def draw_concentric_circles(t, radius, num_circles):
  for i in range(num_circles):
    t.pencolor(random.random(), random.random(), random.random())
    t.circle(radius - i * 10)

def draw_interlocking_squares(t, size):
  for i in range(4):
    t.forward(size)
    t.right(90)
  t.penup()
  t.forward(size / 2)
  t.left(45)
  t.pendown()
  for i in range(4):
    t.forward(size)
    t.right(90)
  t.penup()
  t.backward(size / 2)
  t.right(45)
  t.pendown()

def main():
  t = turtle.Turtle()
  t.speed(0)
  t.hideturtle()

  # Draw concentric circles
  draw_concentric_circles(t, 200, 10)

  # Draw interlocking squares
  t.penup()
  t.goto(0, -100)
  t.pendown()
  t.pencolor("black")
  size = 20
  for i in range(8):
    draw_interlocking_squares(t, size)
    size += 10
    t.penup()
    t.backward(size / 2)
    t.left(45)
    t.pendown()

  turtle.done()

if __name__ == "__main__":
  main()