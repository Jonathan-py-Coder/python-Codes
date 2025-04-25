import pgzrun
from random import randint 
from time import time 

WIDTH=800
HEIGHT=475

star=[]
lines=[]
number_of_stars=8

next_star=0


start_time=0
total_time=0
end_time=0


def create_star():
    global start_time
    for count in range(0,number_of_stars):
        star=Actor("sun")
        star.pos=randint(50,750),randint(50,350)
        star.append(star)
    start_time=time()

def draw():
    global total_time
    screen.blit("bg",(0,0))
    number=1
    for i in star:
        screen.draw.text(str(number),(i.pos[0],i.pos[1]+20))
        i.draw()
        number=number+1


        for line in lines:
            screen.draw.line(line[0],line[1],"cyan")
        if next_star < number_of_stars:
            total_time=time() - start_time
            screen.draw.text(str(round(total_time,1)),(10,10),fontsize=30)
        else:
            screen.draw.text(str(round(total_time,1)),(10,10),fontsize=30)


def update():
    pass

def on_mouse_down(pos):
    global next_star,lines
    if next_star < number_of_stars:
        if sta[next_star].collidepoint(pos):
            if next_star:
                lines.append((star[next_star-1].pos,star[next_star].pos))
            next_star=next_star+1
        else:
            lines=[]
            next_star=0

create_star()
pgzrun.go()