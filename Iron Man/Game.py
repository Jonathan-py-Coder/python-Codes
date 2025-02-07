import pgzrun
from random import randint

TITLE= "Hit Iron Man"

WIDTH=800
HEIGHT=800

message=""

im=Actor("iron man.png")
im.pos=100,100

def draw():
    screen.clear()
    screen.fill(color=("teal"))

    im.draw()
    screen.draw.text(message,center=(400,10),fontsize=30)

def move():
    im.x=randint(50,WIDTH-50)
    im.y=randint(50,WIDTH-50)

def on_mouse_down(pos):
    global message
    if im.collidepoint(pos):
        move()
    else:
        message="you missed"
move()

pgzrun.go()