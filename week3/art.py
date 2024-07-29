import turtle

shelly = turtle.Turtle()

# loop the hexagon
for n in range(36):
    # loop to make hexagon
    for i in range (6):
        shelly.forward(100)
        shelly.left(60)
    shelly.right(10)