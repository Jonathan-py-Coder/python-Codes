#importing the python modulals
import pygame
from time import *
from pygame.locals import *
pygame.init()
#creating the diplay
WIDTH=800
HIGHT=600

screen=pygame.display.set_mode((WIDTH,HIGHT))
#setting up the variables 
pygame.display.set_caption("Understanding Rockets Movement")
player_x=400
player_y=200
keys=[False,False,False,False]
#creating the two images
Rocket=pygame.image.load("Pro Games/Space/rocket1.png")
Rocket=pygame.transform.scale(Rocket,(100,100))

bg=pygame.image.load("Pro Games/Space/space1.jpg")
bg=pygame.transform.scale(bg,(HIGHT,WIDTH))
#creating the main while loop
while player_y<HIGHT:
    screen.blit(bg,(0,0))
    screen.blit(Rocket,(player_x,player_y))
    pygame.display.update()

    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            exit(0)
            #making the controls

        if event.type==pygame.KEYDOWN:

            if event.key==K_UP:
                keys[0]=True
            elif event.key==K_LEFT:
                keys[1]=True
            elif event.key==K_DOWN:
                keys[2]=True
            elif event.key==K_RIGHT:
                keys[3]=True
        if event.type==pygame.KEYUP:
            if event.key==pygame.K_UP:
                keys[0]=False
            elif event.key==pygame.K_LEFT:
                keys[1]=False
            elif event.key==pygame.K_DOWN:
                keys[2]=False
            elif event.key==pygame.K_RIGHT:
                keys[3]=False
    if keys[0]:
        if player_y>0:
            player_y=player_y-7
    elif keys[2]:
        if player_y<550:
            player_y=player_y+7
    if keys[1]:
        if player_x>0:
            player_x=player_x-2
    elif keys [3]:
           if player_x<750:
               player_x=player_x+2
    player_y=player_y+5
    sleep(0.05)
    #creating the you lost the game message
print("you lost the game")
