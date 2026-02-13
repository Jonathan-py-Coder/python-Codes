#importing the pygame module
import pygame
from pygame.locals import *

pygame.init()
#making the constants and veriables
clock=pygame.time.Clock()
FPS=60

SCREEN_WIDTH=864
SCREEN_HEIGHT=936

screen=pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
pygame.display.set_caption("Flappy Bird")

ground_scroll=0
scroll_speed=4
flying=False
game_over=False

#importing images fot the backround
bg=pygame.image.load("Pro Games/FlappyBird/Imagesforflappy/bg.png")
ground_img=pygame.image.load("Pro Games/FlappyBird/Imagesforflappy/ground.png")

class Bird(pygame.sprite.Sprite):
   def __init__(self,x,y):
    pygame.sprite.Sprite.__init__(self)
    self.image=[]
    self.index=0
    self.counter=0
    for i in range(1,4):
        img=pygame.image.load(f"Pro Games/FlappyBird/Imagesforflappy/bird{i}.png")
        self.image.append(img)
    self.image=self.image[self.index]
    self.rect=self.image.get_rect()
    self.rect.center=[x,y]
    self.vel=0
    self.clicked=False

    def update(self):
        if flying == True:
           self.vel = self.vel+0.5
           if self.vel >8:
                self.vel=8
           if self.rect.bottom < 768:
               self.rect.y = self.rect.y + int(self.vel)
        
        if game_over == False:
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                self.vel = -10
            if pygame.mouse.get_pressed()[0] == 0:
                self.clicked = False

            self.counter=self.counter+1
            flap_cooldown=5

            if self.counter > flap_cooldown:
                self.counter =0
                self.index= self.index +1
                if self.index >= len(self.images):
                    self.index=0
            self.image=self.images[self.index]

            self.image=pygame.transform.rotate(self.image[self.index],self.vel*-2)
        else:
            self.image=pygame.transform.rotate(self.image[self.index],-90)


bird_group=pygame.sprite.Group()
flappy=Bird(100,int(SCREEN_HEIGHT/2))
bird_group.add(flappy)

run=True

while run:
    #handeling the clock
    clock.tick(FPS)
    screen.blit(bg,(0,0))

    bird_group.draw(screen)
    bird_group.update()
    #making the ground move
    screen.blit(ground_img,(ground_scroll,768))

    if flappy.rect.bottom > 768:
        game_over = True
        flying=False
    
    if game_over == False:
        ground_scroll=ground_scroll - scroll_speed
        if abs(ground_scroll) > 35:
            ground_scroll=0
    #checking the player quit the game.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
             run=False
        if event.type == pygame.MOUSEBUTTONDOWN and flying == False and game_over == False:
          flying = True

    pygame.display.update()

pygame.quit()