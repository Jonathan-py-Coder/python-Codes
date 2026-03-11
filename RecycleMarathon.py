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
        self.image = pygame.image.load("New folder/RecycleMarathon/Images/bin.png").convert_alpha()
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
        self.image = pygame.image.load("New folder/RecycleMarathon/Images/plastic.png").convert_alpha()
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


    timeElapsed=time.time()-start_time
    if timeElapsed >=60:
        if score >50:
            text=myFont.render("bin loot succesful", True, " red")
            change_Backround("New folder/RecycleMarathon/Images/youwin.jpg")
        else:
            text=myFont.render("Better Luck Next Time",True,"white")
            change_Backround("New folder/RecycleMarathon/Images/youlose.jpg")
    else:
        change_Backround("New folder/RecycleMarathon/Images/bground.png")
        countdown=timingFont.render("Time Left: "+str(60-int(timeElapsed)),True,"white")
        keys=pygame.key.get_pressed()
        if keys[pygame.K_DOWN]:
            if bin.rect.y < 630:
                bin.rect.y +=5
        if keys[pygame.K_UP]:
            if bin.rect.y >0:
                bin.rect -=5

        if keys[pygame.K_LEFT]:
            if bin.rect.x >0:
                bin.rect.x-=5

        if keys[pygame.K_RIGHT]:
            if bin.rect.x <0:
                bin.rect.x+=5

        item_hit_list=pygame.sprite.spritecollide(bin, items_list, True)
        plastic_hit_list=pygame.sprite.spritecollide(bin, plastic_list, True)

        for item in item_hit_list:
            score+=1
            text=myFont.render("Score :"+str(score),True,"white")
        
        for plastic in plastic_hit_list:
            score = score - 5
            text = myFont.render("Score ="+str(score),True,"white")

        screen.blit(text,(20,50))
        allsprites.draw(screen)
    pygame.display.update

pygame.quit()