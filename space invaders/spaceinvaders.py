#Importing Moduals
import pygame
import os
#initialising the font and the mixer
pygame.font.init()
pygame.mixer.init()
#Creating the screen
WIDTH=900
HEIGHT=500

WIN=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("First Game!")
#Creating a border for the space ships
BORDER=pygame.Rect(WIDTH//2 -5,0,10,HEIGHT)

HEALTH_FONT=pygame.font.SysFont("Times New Roman",40)
WINNER_FONT=pygame.font.SysFont("Times New Roman",100)
#Creating varibles
FPS=60
VEL=5
BULLET_VEL=7
MAX_BULLETS=3
SPACESHIP_HEIGHT=40
SPACESHIP_WIDTH=55

YELLOW_HIT=pygame.USEREVENT +1
RED_HIT=pygame.USEREVENT +2
#Loading in the spaceship and backround
YELLOW_SPACESHIP_IMAGE=pygame.image.load("Pro Games/space invaders/spaceship_yellow.png")
YELLOW_SPACESHIP=pygame.transform.rotate(pygame.transform.scale(YELLOW_SPACESHIP_IMAGE,(SPACESHIP_WIDTH,SPACESHIP_HEIGHT)),90)
RED_SPACESHIP_IMAGE=pygame.image.load("Pro Games/space invaders/spaceship_red.png")
RED_SPACESHIP=pygame.transform.rotate(pygame.transform.scale(RED_SPACESHIP_IMAGE,(SPACESHIP_WIDTH,SPACESHIP_HEIGHT)),270)

SPACE=pygame.transform.scale(pygame.image.load("Pro Games/space invaders/space.png"),(WIDTH,HEIGHT))
#Creating the window
def draw_window(red,yellow,red_bullets,yellow_bullets,red_health,yellow_health):
    WIN.blit(SPACE,(0,0))
    pygame.draw.rect(WIN,"Black",BORDER)

    red_health_text=HEALTH_FONT.render("Health: "+str(red_health),1,1,"white")
    yellow_health_text=HEALTH_FONT.render("Health: "+str(yellow_health),1,1,"white")

    WIN.blit(red_health_text,(WIDTH-red_health_text.get_width() -10,10))
    WIN.blit(yellow_health_text,(10,10))

    WIN.blit(YELLOW_SPACESHIP,(yellow.x,yellow.y))
    WIN.blit(RED_SPACESHIP,(red.x,red.y))

    for bullet in red_bullets:
        pygame.draw.rect(WIN,"red",bullet)
    for bullet in yellow_bullets:
        pygame.draw.rect(WIN,"yellow",bullet)
    
    pygame.display.update()
#Crating the keys to move the space ships
def yellow_handle_movement(keys_pressed,yellow):
    if keys_pressed[pygame.K_a] and yellow.x - VEL > 0:
        yellow.x=yellow.x- VEL
    if keys_pressed[pygame.K_d] and yellow.x + VEL + yellow.width<BORDER.x:
        yellow.x = yellow.x+VEL
    if keys_pressed[pygame.K_w] and yellow.y - VEL > 0:
        yellow.y=yellow.y - VEL
    if keys_pressed[pygame.K_s] and yellow.y + VEL +yellow.height < HEIGHT-15:
        yellow.y = yellow.y + VEL
    
def red_handle_movement(keys_pressed,red):
    if keys_pressed[pygame.K_LEFT] and red.x - VEL > 0:
        red.x=red.x- VEL
    if keys_pressed[pygame.K_RIGHT] and red.x + VEL + red.width<WIDTH:
        red.x = red.x+VEL
    if keys_pressed[pygame.K_UP] and red.y - VEL > 0:
        red.y=red.y - VEL
    if keys_pressed[pygame.K_DOWN] and red.y + VEL+ red.height < HEIGHT+15:
        red.y = red.y + VEL
#Creating bullets
def handel_bullets(yellow_bullets, red_bullets,yellow,red):
    for bullet in yellow_bullets:
        bullet.x =bullet.x+BULLET_VEL
        if red.colliderect(bullet):
            pygame.event.post(pygame.event.Event(RED_HIT))
    
        elif bullet.x > WIDTH:
            yellow_bullets.remove(bullet)

    for bullet in red_bullets:
        bullet.x =bullet.x-BULLET_VEL
        if yellow.colliderect(bullet):
            pygame.event.post(pygame.event.Event(YELLOW_HIT))
            red_bullets.remove(bullet)
        elif bullet.x > WIDTH:
            red_bullets.remove(bullet)
#Creating the winner text
def draw_winner(text):
    draw_text=WINNER_FONT.render(text,1,"White")
    WIN.blit(draw_text,(WIDTH/2 -draw_text.get_width()/2,HEIGHT/2-draw_text.get_height()/2))
    pygame.display.update()
    pygame.time.delay(5000)
#Creating the main code.
def main():
    red=pygame.Rect(700,300,SPACESHIP_WIDTH,SPACESHIP_HEIGHT)
    yellow=pygame.Rect(100,300,SPACESHIP_WIDTH,SPACESHIP_HEIGHT)

    red_bullets=[]
    yellow_bullets=[]

    red_health=10
    yellow_health=10
    clock=pygame.time.Clock()
    run=True
    
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run=False
                pygame.quit()
    
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LCTRL and len(yellow_bullets) < MAX_BULLETS:
                    bullet=pygame.Rect(yellow.x+yellow.width, yellow.y+yellow.height //2-2,10,5)
                    yellow_bullets.append(bullet)

                if event.key == pygame.K_RCTRL and len(red_bullets) < MAX_BULLETS:
                    bullet=pygame.Rect(red.x,red.y+red.height//2-2,10,5)
                    red_bullets.append(bullet)
                
            if event.type == RED_HIT:
                red_health = red_health-1

            if event.type == YELLOW_HIT:
                yellow_health = yellow_health-1
                
        winner_text=""
        if red_health<=0:
            winner_text="Yellow Wins!!"
            
        if yellow_health <=0:
            winner_text="Red Wins!!"

        if winner_text !="":
            draw_winner(winner_text)
            break
            
        keys_pressed=pygame.key.get_pressed()
        yellow_handle_movement(keys_pressed,yellow)
        red_handle_movement(keys_pressed,red)

        handel_bullets(yellow_bullets,red_bullets,yellow,red)
        draw_window(red,yellow,red_bullets,yellow_bullets,red_health,yellow_health)
#runing the main function
    main()
if __name__ == "__main__":
    main()