import pgzrun
from random import randint 

WIDTH=800
HEIGHT=475

satellites=[]
lines=[]
number_of_satellites=8

next_satellite=0
def draw():
    screen.blit("bg",(0,0))
    number=1
    for i in satellites:
        screen.draw.text(str(number),(i.pos[0],i.pos[1]+20))
        i.draw()
        number=number+1

def create_satellites():
    for count in range(0,number_of_satellites):
        satellite=Actor("satellite")
        satellite.pos=randint(50,750),randint(50,350)
        satellites.append(satellite)
    for line in lines:
        screen.draw.line(line[0],line[1],("cyan"))

def update():
    pass
def on_mouse_down(pos):
    global next_satellite,lines
    if next_satellite < number_of_satellites:
        if satellites[next_satellite].collidepoint(pos):
            if next_satellite:
                lines.append(satellites[next_satellite-1].pos,satellites[next_satellite].pos)
        else:
            lines=[]
            next_satellite=0

create_satellites()
pgzrun.go()