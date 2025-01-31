import pgzrun
from random import randint

WIDTH=300
HIGHT=300

def draw():
    color="orange"
    w=WIDTH
    h=HIGHT-200
    for i in range(20):
        r=randint(0,255)
        g=randint(0,255)
        b=randint(0,255)
        rect=Rect((0,0),(w,h))
        rect.center=150,150
        screen.draw.filled_rect(rect,(r,g,b))
        w=w-10
        h+=10

    

pgzrun.go()