import turtle

# make list of colors
colors = ["red", "green", "blue", "yellow", "white"]

# set a background color
turtle.bgcolor("black")

# set a var for turtle for ease of use later
shelly = turtle.Turtle()

# set speed to 0 to save time
shelly.speed(0)

# loop the hexagon
for n in range(36):
    # loop to make hexagon
    for i in range (6):
        shelly.color(colors[i])
        shelly.forward(100)
        shelly.left(60)
    shelly.right(10)

# make circles
shelly.penup()
shelly.color("white")

for i in range (36):
    shelly.forward(220)
    shelly.pendown()
    shelly.circle(5)
    shelly.penup()
    shelly.backward(220)
    shelly.right(10)

shelly.hideturtle()