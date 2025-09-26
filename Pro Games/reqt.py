import pygame

pygame.init()

screen=pygame.display.set_mode((600,600))

screen.fill("black")

pygame.display.update()

class Rect():
    def __init__(self,color,dimensions):
        self.rect_surf=screen
        self.rect_color=color
        self.rect_dimentions=dimensions

    def draw(self):
        self.draw_Reqt=pygame.draw.rect(self.rect_surf,self.rect_color,self.rect_dimentions)


greenrect=Rect("green",(50,20,100,100))
redrect=Rect("red",(150,200,150,150))
bluerect=Rect("blue",(300,400,200,200))
purplerect=Rect("purple",(250,430,280,120))
whiterect=Rect("white",(250,150,50,25))

greenrect.draw()
bluerect.draw()
redrect.draw()
purplerect.draw()
whiterect.draw()

pygame.display.update()

pygame.time.delay(5000)

pygame.quit()