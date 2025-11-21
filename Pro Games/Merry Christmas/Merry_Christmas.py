import pygame
import time
pygame.init()

WIDTH=800
HEIGHT=600

screen=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Birthday Greeting Card")

image1=pygame.image.load("Pro Games/Merry Christmas/image1.jpg")
image1=pygame.transform.scale(image1,(WIDTH,HEIGHT))

image2=pygame.image.load("Pro Games/Merry Christmas/Image2.jpg")
image2=pygame.transform.scale(image2,(WIDTH,HEIGHT))


image3=pygame.image.load("Pro Games/Merry Christmas/image3.jpg")
image3=pygame.transform.scale(image3,(WIDTH,HEIGHT))

image4=pygame.image.load("Pro Games/Merry Christmas/Image4.jpg")
image4=pygame.transform.scale(image4,(WIDTH,HEIGHT))

image5=pygame.image.load("Pro Games/Merry Christmas/Image5.jpg")
image5=pygame.transform.scale(image5,(WIDTH,HEIGHT))

gameload=True
while gameload:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameload=False
    font=pygame.font.SysFont("Ariel",40)

    t1=font.render("Marry Christmas and a Happy New Year", True,"black")
    screen.blit(image1,(0,0))
    screen.blit(t1,(200,200))
    pygame.display.update()
    time.sleep(2)

    t2=font.render("Wish you a bright future over the next year",True,"black")
    
    screen.blit(image2,(0,0))
    screen.blit(t2,(200,200))
    pygame.display.update()
    time.sleep(2) 

    t3=font.render("Hope you have a fun year ahead",True,"black")
    
    screen.blit(image3,(0,0))
    screen.blit(t3,(200,200))
    pygame.display.update()
    time.sleep(2) 

    t4=font.render("Hoping Your Chistmas wishes become true",True,"black")
    
    screen.blit(image4,(0,0))
    screen.blit(t4,(200,200))
    pygame.display.update()
    time.sleep(2) 

    t5=font.render("Hoping you have a wonderfull ",True,"black")
    t6=font.render( "amount of presents",True,"black")
    
    screen.blit(image5,(0,0))
    screen.blit(t5,(200,200))
    screen.blit(t6,(200,220))
    pygame.display.update()
    time.sleep(2) 

pygame.quit()