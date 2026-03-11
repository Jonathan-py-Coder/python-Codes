import pygame
import time
from pygame.locals import *
import random
pygame.init()


WIDTH=900
HEIGHT=700

def change_Backround(img):
    backround=pygame.image.load(img)
    bg= pygame.transform.scale(backround, (WIDTH,HEIGHT))
    screen.blit(bg,(0, 0))


pygame.display.set_caption("Recycle Marathon")

screen = pygame.display.set_mode([WIDTH,HEIGHT])

class Bin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("RecycleMarathon/Images/bin.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (40, 60))
        self.rect = self.image.get_rect()

class Recyclable(pygame.sprite.Sprite):
    def __init__(self,img):
        super().__init__()
        self.image = pygame.image.load(img).convert_alpha()
        self.image = pygame.transform.scale(self.image, (30, 30))
        self.rect = self.image.get_rect()

class Non_Recycable(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("RecycleMarathon/Images/plastic.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (40, 40))
        self.rect = self.image.get_rect()

images=["item1.png","item2.png","item3.png"]
items_list=pygame.sprite.Group()
allsprites = pygame.sprite.Group()
plastic_list=pygame.sprite.Group()

for i in range(20):
    plastic=Non_Recycable()
    plastic.rect.x = random.randrange(WIDTH)
    plastic.rect.y = random.randrange(HEIGHT)
    plastic_list.add(plastic)
    allsprites.add(plastic)

bin=Bin()
allsprites.add(bin)
playing = True
score=0
clock=pygame.time.Clock()

start_time=time.time()

myFont=pygame.font.SysFont("Times New Roman", 22)
timingFont=pygame.font.SysFont("Times New Roman", 22)
text=myFont.render("Score ="+str(0),True,"white")

while playing:
    clock.tick(30)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            playing = False


    timeelapsed=time.time()-start_time
    if timeelapsed >=60:
        if score >50:
            text=myFont.render("bin loot succesful", True, " red")
            screen.blit("youwin.jpg",(0,0))

pygame.quit()