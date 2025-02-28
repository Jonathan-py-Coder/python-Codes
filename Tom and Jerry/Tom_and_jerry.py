import pgzrun
from random import randint

WIDTH=1600
HEIGHT=1600
tom=Actor("tom")
tom.pos=200,200

jerry=Actor("jerry")
jerry.pos=800,800

score=0
game_over=False


def draw():
    screen.clear()
    screen.fill(color=("black"))

    tom.draw()
    jerry.draw()

    screen.draw.text("score ="+str(score),color="pink",topleft=(10,10))

    if game_over:
        screen.fill("pink")
        screen.draw.text("timers up your final score is"+str(score),midtop=(WIDTH/2,10),fontsize=40,color="black")
def place_jerry():
    jerry.x=randint(50,WIDTH-50)
    jerry.y=randint(50,HEIGHT-50)

def time_up():
    global game_over
    game_over=True
def update():
    global score
    if keyboard.left:
        tom.x=tom.x-2
    if keyboard.right:
        tom.x=tom.x+2    
    if keyboard.up:
        tom.y=tom.y-2
    if keyboard.down:
        tom.y=tom.y+2        

    jerry_collected=tom.colliderect(jerry)
    
    if jerry_collected:
        score=score+10
        place_jerry()

clock.schedule(time_up,6000)
pgzrun.go()