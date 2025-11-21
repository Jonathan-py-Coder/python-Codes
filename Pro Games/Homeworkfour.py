import pygame

pygame.init()

screen=pygame.display.set_mode((800,800))

screen.fill("pink")

pygame.display.update()

class Sqre():
    def __init__(self,color,dimensions):
        self.sqre_surf=screen
        self.sqre_color=color
        self.sqre_dimentions=dimensions

    def draw(self):
        self.draw_Reqt=pygame.draw.rect(self.sqre_surf,self.sqre_color,self.sqre_dimentions)


    
bluesqre=Sqre("blue",(670,30,0,432))
pinksqre=Sqre("pink",(300,200,50,123))
redsqre=Sqre("red",(600,700,400,400))
lightgreensqre=Sqre("lightgreen",(650,200,375,456))
purplesqre=Sqre("purple",(400,500,40,30))

bluesqre.draw()
pinksqre.draw()
redsqre.draw()
lightgreensqre.draw()
purplesqre.draw()





pygame.display.update()

pygame.time.delay(5000)

pygame.quit()