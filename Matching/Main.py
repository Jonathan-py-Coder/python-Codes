import pygame

pygame.init()

WIDTH=1000
HEIGHT=700

screen=pygame.display.set_mode((WIDTH,HEIGHT),)
pygame.display.set_caption("Match it!!")

Candy_Crush=pygame.image.load("Pro Games/Matching/Images/Candy Crush.png")
Candy_Crush=pygame.transform.scale(Candy_Crush,(80,80))

Clash_of_Clans=pygame.image.load("Pro Games/Matching/Images/Clash of Clans.png")
Clash_of_Clans=pygame.transform.scale(Clash_of_Clans,(80,80))

Clash_Royal=pygame.image.load("Pro Games/Matching/Images/Clash Royal.png")
Clash_Royal=pygame.transform.scale(Clash_Royal,(80,80))

Subway_Surfers=pygame.image.load("Pro Games/Matching/Images/Subway Surfers.png")
Subway_Surfers=pygame.transform.scale(Subway_Surfers,(80,80))

Temple_Run=pygame.image.load("Pro Games/Matching/Images/Temple Run.png")
Temple_Run=pygame.transform.scale(Temple_Run,(80,80))

screen.blit(Candy_Crush,(50,100))
screen.blit(Clash_of_Clans,(50,200))
screen.blit(Clash_Royal,(50,300))
screen.blit(Subway_Surfers,(50,400))
screen.blit(Temple_Run,(50,500))

f=pygame.font.SysFont("Times New Roman",40)

text1=f.render("Candy_Crush",True,"white")
text2=f.render("Clash_of_Clans",True,"green")
text3=f.render("Clash_Royal",True,"blue")
text4=f.render("Subway_Surfers",True,"purple")
text5=f.render("Temple_Run",True,"red")

screen.blit(text1,(350,100))
screen.blit(text2,(350,200))
screen.blit(text3,(350,300))
screen.blit(text4,(350,400))
screen.blit(text5,(350,500))

pygame.display.update()

while 1:
    event = pygame.event.poll()

    if event.type == pygame.MOUSEBUTTONDOWN:
        pos=pygame.mouse.get_pos()
        pygame.draw.circle(screen,"white",pos,20,0)
        pygame.display.update()

    elif event.type == pygame.MOUSEBUTTONUP:
        pos2=pygame.mouse.get_pos()
        pygame.draw.line(screen,"white",(pos),(pos2),5)
        pygame.draw.circle(screen,"white",pos2,20,0)
        pygame.display.update()

