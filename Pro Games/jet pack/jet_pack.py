import pygame
pygame.init()
from time import *
from pygame.locals import *

WIDTH=800
HIGHT=600

screen=pygame.display.set_mode((WIDTH,HIGHT))

pygame.display.set_caption("Understanding the movement of the jetpack Movement")
player_x=400
player_y=200
keys=[False,False,False,False]

jetpack=pygame.image.load("Pro Games/jet pack/jetpack.png")
jetpack=pygame.transform.scale(jetpack,(100,100))

bg=pygame.image.load("Pro Games/jet pack/bg.png")
bg=pygame.transform.scale(bg,(HIGHT,WIDTH))

while player_y<HIGHT:
    screen.blit(bg,(0,0))
    screen.blit(jetpack,(player_x,player_y))
    pygame.display.update()

    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            exit(0)
        

        if event.type==pygame.KEYDOWN:

            if event.key==K_w:
                keys[0]=True
            elif event.key==K_a:
                keys[1]=True
            elif event.key==K_s:
                keys[2]=True
            elif event.key==K_d:
                keys[3]=True
        if event.type==pygame.KEYUP:
            if event.key==pygame.K_w:
                keys[0]=False
            elif event.key==pygame.K_a:
                keys[1]=False
            elif event.key==pygame.K_s:
                keys[2]=False
            elif event.key==pygame.K_d:
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
    
print("you lost the game")
