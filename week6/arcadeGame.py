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

# update score
def update_score_level():
    global score, level, candy_speed
    score += 1
    score_display.config(text='Score : ' + str(score))
    # determine if level changes
    # update level and candy speed
    if score > 5 and score <=10:
        candy_speed += 1
        level = 2
        level_display.config(text='Level : ' + str(level))
    elif score > 10:
        candy_speed += 1
        level = 3
        level_display.config(text='Level : ' + str(level))

# check for candy impact
def collision(item1, item2, distance):
    xdistance = abs(canvas.coords(item1)[0] - canvas.coords(item2)[0])
    ydistance = abs(canvas.coords(item1)[1] - canvas.coords(item2)[1])
    overlap = xdistance < distance and ydistance < distance
    return overlap

# check if character hit bad candy, schedule game_over
# if player impacts candy remove from screen, list, update score
def check_hits():
    for candy in bad_candy_list:
        if collision(mychar, candy, 30):
            game_over = canvas.create_text(200,200,text='Game Over',fill='red', font = ('Helvetica', 30))
            window.after(1000, end_game)
            return
    for candy in candy_list:
        if collision(mychar, candy, 30):
            canvas.delete(candy)
            candy_list.remove(candy)
            update_score_level()
    window.update(100, check_hits)

move_direction = 0

# initial key press function
def check_input(event):
    global move_direction
    key = event.keysym
    if key == "Right":
        move_direction = "Right"
    elif key == "Left":
        move_direction = "Left"
    
# end button press
def end_input(event):
    global move_direction
    move_direction = "None"

# check for edge of window and move
def move_char():
    if move_direction == "Right" and canvas.coords(mychar)[0] < 400:
        canvas.move(mychar, 10, 0)
    if move_direction == "Left" and canvas.coords(mychar)[0] > 0:
        canvas.move(mychar, -10, 0)
    window.after(16, move_char)

# bind movements
canvas.bind_all('<KeyPress>', check_input)
canvas.bind_all('<KeyRelease>', end_input)

# end game function
def end_game():
    window.destroy()

# remove instructions
def end_title():
    canvas.delete(title)
    canvas.delete(directions)

# schedule funtions to run
window.after(1000, end_title)
window.after(1000, make_candy)
window.after(1000, move_candy)
window.after(1000, check_hits)
window.after(1000, move_char)

# GUI main event loop
window.mainloop()