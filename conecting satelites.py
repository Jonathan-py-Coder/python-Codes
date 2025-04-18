import pgzrun
from random import randint 
from time import time 

WIDTH=800
HEIGHT=475

satellites=[]
lines=[]
number_of_satellites=8

next_satellite=0
#Makeing the veriables for time
start_time=0
total_time=0
end_time=0
#Makeing the function for creationg the satelltes 
def create_satellites():
    global start_time
    for count in range(0,number_of_satellites):
        satellite=Actor("satellite")
        satellite.pos=randint(50,750),randint(50,350)
        satellites.append(satellite)
    start_time=time()

def draw():
    global total_time
    screen.blit("bg",(0,0))
    number=1
    for i in satellites:
        screen.draw.text(str(number),(i.pos[0],i.pos[1]+20))
        i.draw()
        number=number+1
#MAKEING THE LINES TO CONNECT THE SATTELITES 
        for line in lines:
            screen.draw.line(line[0],line[1],"cyan")
        if next_satellite < number_of_satellites:
            total_time=time() - start_time
            screen.draw.text(str(round(total_time,1)),(10,10),fontsize=30)
        else:
            screen.draw.text(str(round(total_time,1)),(10,10),fontsize=30)



    
#the game is updated
def update():
    pass
#this checks if you clicked the satellite in the correct order
def on_mouse_down(pos):
    global next_satellite,lines
    if next_satellite < number_of_satellites:
        if satellites[next_satellite].collidepoint(pos):
            if next_satellite:
                lines.append((satellites[next_satellite-1].pos,satellites[next_satellite].pos))
            next_satellite=next_satellite+1
        else:
            lines=[]
            next_satellite=0

create_satellites()
pgzrun.go()