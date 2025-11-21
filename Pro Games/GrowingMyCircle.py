#importing the moduals
import pygame

pygame.init()
#creating the varibles
WIDTH=600
HIGHT=600

screen=pygame.display.set_mode((WIDTH,HIGHT))
pygame.display.set_caption("Grow My Circle")

gameloop=True
#creating the circle class
class Circle():
    def __init__(self,colour,pos,radius,width):
        self.cc=colour
        self.cp=pos
        self.cr=radius
        self.cw=width
        self.cs=screen

    def draw(self):
        self.Draw_Circle=pygame.draw.circle(self.cs,self.cc,self.cp,self.cr,self.cw)
            
    def grow(self,r):
        self.cr=self.cr+r
        self.Draw_Circle=pygame.draw.circle(self.cs,self.cc,self.cp,self.cr,self.cw)
#creating the circles
c=Circle("blue",(300,300),25,0)

#creating while loop and the events

while gameloop:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameloop=False

        if event.type == pygame.MOUSEBUTTONDOWN:
            screen.fill("black")
            c.draw()
            pygame.display.update()
        
        elif event.type == pygame.MOUSEBUTTONUP:
            screen.fill("black")
            c.grow(20)
            pygame.display.update()




pygame.quit()