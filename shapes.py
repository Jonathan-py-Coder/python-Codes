import pgzrun

WIDTH=600
HEIGHT=600

def draw():

    screen.draw.circle((200,200),50,"hot pink")

    screen.draw.filled_circle((300,300),50,"cyan")
    rect=Rect((200,300),(50,100))
    screen.draw.rect(rect,"green")

    screen.draw.filled_rect(rect,"blue")

pgzrun.go()