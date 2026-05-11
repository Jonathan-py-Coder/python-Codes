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

img=r"MineSweeper/Block.png"
blockimg=pygame.image.load(img)

class Block(pygame.sprite.Sprite):
     def __init__(self, img, x, y):
          super().__init__()
          self.image=pygame.image.load(img)
          self.image = pygame.transform.scale(self.image, (70,70))
          self.imagetype ="block"
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

def make_mines():
     for bombs in range(15):
          row=random.randint(0,9)
          colum=random.randint(0,9)
          matrix[row][colum]="M"
     print(matrix)

make_mines()
def reset():
          global Starttime
          for row in range(10):
               for colum in range(10):
                    matrix[row][colum] = 0
          for block in BlocksGroup:
               block.image=blockimg
          make_mines()
          Starttime=time.time()



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
               if pygame.mouse.get_pressed()[0]:
                    if matrix[row][colum]=="M":
                         block.image=pygame.image.load(r"MineSweeper/bomb_exploded.png")
                         block.imagetype="mine"
                         pygame.display.update()
                         pygame.time.delay(2000)
                         reset()
                         return

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
                         block.imagetype="numbers"
               elif pygame.mouse.get_pressed()[2]:
                    block.image=pygame.image.load(r"MineSweeper/flag.png")
                    block.imagetype="flag"

gamefinished=False

win=True
def areminesflags():
     global win
     win=True
     for row in range(10):
          for colum in range(10):
               if matrix[row][colum]=="M":
                    if block.imagetype=="flag":
                         pass
                    else:
                         win=False
               else:
                    pass



def checkend():
     global gamefinished
     gamecomplete=True
     
     for row in range(10):
          for colum in range(10):
               num=row * 10
               num=num+colum
               if BlocksGroup.sprites()[num].imagetype == "block":
                     gamecomplete=False    

     if gamecomplete==True:
          areminesflags()
          if win==True:
               print("complete")
               gamefinished=True         

            

while Running:
     screen.fill("lightgray")
     BlocksGroup.draw(screen)
     for event in pygame.event.get():
          if event.type == pygame.QUIT:
              Running = False
          if event.type==pygame.MOUSEBUTTONDOWN:
               mousepos=pygame.mouse.get_pos()
               mouse_pressed(mousepos)
               checkend()
     if gamefinished == False:   
          timetaken = time.time()-Starttime
     
     font=pygame.font.SysFont("Times New Roman",50)

     timefont=font.render("Time Taken - "+str(round(timetaken,0)),True,(255,255,255))

     screen.blit(timefont, (250, 20))
     pygame.display.update()
    
pygame.quit()