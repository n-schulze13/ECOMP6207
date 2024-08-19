from tkinter import *
import random

# make a window
window = Tk()
window.title('The Candy Monster Game')

# create a canvas to put objects on screen
canvas = Canvas(window, width=400,height=400,bg='black')
canvas.pack()

# set up welcome screen with title and directions
title = canvas.create_text(200, 200, text= 'The Candy Monster', fill='white', font=('Helvetica', 30))
directions = canvas.create_text(200, 300, text='Collect Candy but avoid the red ones!', fill='white', font=('Helvetica', 20))

# score display with widget
score = 0
score_display = Label(window, text='Score : ' + str(score))
score_display.pack()

# level with widget
level = 1
level_display = Label(window, text='Score : ' + str(level))
level_display.pack()

# create image object
player_image = PhotoImage(file='greenChar.gif')

# use image to create character
mychar = canvas.create_image(200, 360, image=player_image)

# make variables and lists
candy_list = []
bad_candy_list = []
candy_speed = 2
candy_color_list = ['red', 'yellow', 'purple', 'green', 'blue', 'pink', 'white']

# random candy function
def make_candy():
    xposition = random.randint(1,400)
    candy_color = random.choice(candy_list)
    candy = canvas.create_oval(xposition, 0, xposition+30, fill = candy_color)
    candy_list.append(candy)
    if candy_color == 'red':
        bad_candy_list.append(candy)
    window.after(1000,make_candy)

# move the candy
def move_candy():
    for candy in candy_list:
        canvas.move(candy, 0, candy_speed)
        if canvas.coords(candy)[1] > 400:
            xposition = random.randint(1,400)
            canvas.coords(candy,xposition, 0, xposition+30, 30)
    window.after(50, move_candy)

# GUI main event loop
window.mainloop()