import pygame
import time
pygame.init()

HEIGHT=800
WIDTH=450

screen=pygame.display.set_mode((WIDTH,HEIGHT))
caption=pygame.display.set_caption("Birthday Cards")

Card1=pygame.image.load("Birthday_Cards/Card1.png")
Card1=pygame.transform.scale(Card1,(WIDTH,HEIGHT))

Card2=pygame.image.load("Birthday_Cards/Card2.png")
Card2=pygame.transform.scale(Card2,(WIDTH,HEIGHT))

Card3=pygame.image.load("Birthday_Cards/Card3.jpg")
Card3=pygame.transform.scale(Card3,(WIDTH,HEIGHT))

Card4=pygame.image.load("Birthday_Cards/Card4.jpg")
Card4=pygame.transform.scale(Card4,(WIDTH,HEIGHT))

sound1=pygame.mixer.Sound("Birthday_Cards/Backround_Music.mp3")



Running=True

while Running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Running=False

    screen.blit(Card1,(0,0))
    pygame.display.update()
    sound1.play()
    time.sleep(10)

    screen.blit(Card1,(0,0))
    pygame.display.update()
    time.sleep(10)

    screen.blit(Card3,(0,0))
    pygame.display.update()
    time.sleep(10)

    screen.blit(Card4,(0,0))
    pygame.display.update()
    time.sleep(10)

pygame.quit()