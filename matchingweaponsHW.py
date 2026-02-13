import pygame
pygame.init()

HEIGHT=800
WIDTH=1000

screen=pygame.display.set_mode((WIDTH,HEIGHT))


pygame.display.set_caption("Match the weapon to the character")


Wizard=pygame.image.load("Pro Games/matchingweapons.py/images/Wizard.png")
Wizard=pygame.transform.scale(Wizard,(80,80))

wand=pygame.image.load("Pro Games/matchingweapons.py/images/wand.png")
wand=pygame.transform.scale(wand,(80,80))

Archer=pygame.image.load("Pro Games/matchingweapons.py/images/Archer.png")
Artcher=pygame.transform.scale(Archer,(0.000001,0.00000001))

Bow=pygame.image.load("Pro Games/matchingweapons.py/images/Bow_and_Arrow.png")
Bow=pygame.transform.scale(Bow,(80,80))

Ninja=pygame.image.load("Pro Games/matchingweapons.py/images/Ninja.png")
Ninja=pygame.transform.scale(Ninja,(80,80))

katana=pygame.image.load("Pro Games/matchingweapons.py/images/Katana.png")
katana=pygame.transform.scale(katana,(80,80))

screen.blit(Wizard,(50,100))
screen.blit(wand,(870,100))
screen.blit(Archer,(50,310))
screen.blit(Bow,(870,310))
screen.blit(Ninja,(50,550))
screen.blit(katana,(870,550))

pygame.display.update()

while True:
    event=pygame.event.poll()
    if event.type == pygame.MOUSEBUTTONDOWN:
        pos=pygame.mouse.get_pos()
        

     
    elif event.type == pygame.MOUSEBUTTONUP:
        
        pos2=pygame.mouse.get_pos()
        if pos == Wizard:
            if pos2 == wand:
                colour2=pygame.color(0,255,0)
        pygame.draw.circle(screen,colour2,pos,20.0)
        pygame.display.update()
        pygame.draw.line(screen,colour2,(pos),(pos2),5)
        pygame.draw.circle(screen,"blue",pos2,20.0)
        pygame.display.update()