import pygame
import random
import time
pygame.init()

WIDTH=800
HEIGHT=900


caption=pygame.display.set_caption("Minesweeper")
screen=pygame.display.set_mode((WIDTH,HEIGHT))

score=0
Starttime=time.time()


Running=True

img="MineSweeper/Block.png"

class Block(pygame.sprite.Sprite):
     def __init__(self, img, x, y):
          super().__init__()
          self.image=pygame.image.load(img)
          self.image = pygame.transform.scale(self.image, (70,70))
          self.rect=self.image.get_rect()
          self.rect.x=x
          self.rect.y=y


BlocksGroup=pygame.sprite.Group()
y=20

matrix=[]



for rows in range(10):
     row=[]
     y=y+80
     x=-75
     for colum in range(10):
          x=x+80
          block=Block(img,x,y)
          BlocksGroup.add(block)
          row.append(0)
     matrix.append(row)


for bombs in range(15):
     row=random.randint(0,9)
     colum=random.randint(0,9)
     matrix[row][colum]="M"
print(matrix)

def mouse_pressed(pos):
     global Running 
#      for rows in range(10):
#           for colum in range(10):
#                if matrix[row][colum]
     for block in BlocksGroup:
          if block.rect.collidepoint(pos):
               colum=block.rect.x//80
               row=block.rect.y//80-1
               print(row,colum)
               if matrix[row][colum]=="M":
                    Running=False
               else:
                    mines=0
                    for r in range(row-1,row+2,1):
                         if r < 0 or r > 9:
                              continue
                         for c in range(colum-1,colum+2,1):
                              if c < 0 or c > 9:
                                   continue
                              if matrix[r][c]=="M":
                                   mines=mines+1
                    
                    block.image=pygame.image.load(r"MineSweeper/"+str(mines)+".png")

while Running:
     screen.fill("lightgray")
     BlocksGroup.draw(screen)
     for event in pygame.event.get():
          if event.type == pygame.QUIT:
              Running = False
          if event.type==pygame.MOUSEBUTTONDOWN:
               mousepos=pygame.mouse.get_pos()
               mouse_pressed(mousepos)
               
     timetaken = time.time()-Starttime
     
     font=pygame.font.SysFont("Times New Roman",50)
     scorefont=font.render(f"Score: {score}", True, (255, 255, 255))
     timefont=font.render("Time Taken - "+str(round(timetaken,0)),True,(255,255,255))
     screen.blit(scorefont, (50,20))
     screen.blit(timefont, (300, 20))
     pygame.display.update()
    
pygame.quit()