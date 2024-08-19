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

# GUI main event loop
window.mainloop()