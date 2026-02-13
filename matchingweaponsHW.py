import pygame
pygame.init()

HEIGHT=800
WIDTH=1000

screen=pygame.display.set_mode((WIDTH,HEIGHT))


pygame.display.set_caption("Match the weapon to the character")
font=pygame.font.SysFont("Times New Roman",50)

Wizard=pygame.image.load("Pro Games/matchingweapons.py/images/Wizard.png")
Wizard=pygame.transform.scale(Wizard,(80,80))

wand=pygame.image.load("Pro Games/matchingweapons.py/images/wand.png")
wand=pygame.transform.scale(wand,(80,80))

Archer=pygame.image.load("Pro Games/matchingweapons.py/images/Archer.png")
Archer=pygame.transform.scale(Archer,(80,80))

Bow=pygame.image.load("Pro Games/matchingweapons.py/images/Bow_and_Arrow.png")
Bow=pygame.transform.scale(Bow,(80,80))

Ninja=pygame.image.load("Pro Games/matchingweapons.py/images/Ninja.png")
Ninja=pygame.transform.scale(Ninja,(80,80))

katana=pygame.image.load("Pro Games/matchingweapons.py/images/Katana.png")
katana=pygame.transform.scale(katana,(80,80))

left_items = {
    "Wizard": (50,100),
    "Archer":(50,310),
    "Ninja":(50,550),
}

right_items = {
    "wand":(870,100),
    "Bow":(870,310),
    "katana":(870,550),
}

matches = {
    "wizard":"wand",
    "archer":"bow",
    "ninja":"katana",
}

left_points = {
    "wizard": (150,190),
    "archer": (150,390),
    "ninja" : (150,590),
}

right_points = {
    "wand":(850,190),
    "bow" :(850,390),
    "katana":(850,590),
}

def make_rect(pos):
    return pygame.Rect(pos[0],pos[1], 80,80)

left_rects = {k: make_rect(v) for k, v in left_items.items()}
right_rects = {k: make_rect(v) for k, v in right_items.items()}

selected_left=None
selected_right=None
lines = []

pygame.display.update()
running=True
while running:

    title = font.render("Match the weapon to the character",True,"black")
    screen.blit(title, (200,40))

    screen.blit(Wizard,left_items["Wizard"])
    screen.blit(Archer,left_items["Archer"])
    screen.blit(Ninja,left_items["Ninja"])

    screen.blit(wand, right_items["wand"])
    screen.blit(Bow, right_items["Bow"])
    screen.blit(katana, right_items["katana"])
    for p in left_points.values():
        pygame.draw.circle(screen,"black", p, 10)

    for p in right_points.values():
        pygame.draw.circle(screen, "black", p, 10)

    for line in lines:
        pygame.draw.line(screen, line["colour"], line["start"], line["end"], 5)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    event=pygame.event.poll()
    if event.type == pygame.MOUSEBUTTONDOWN:
        mouse = pygame.mouse.get_pos()
        
        for name, rect in left_rects():
            if rect.collidepoint(mouse):
                selected_left = name
        for name, rect in right_rects:
            if rect.collidepoint(mouse):
                selected_right = name

        if selected_left and selected_right:
            if matches[selected_left]== selected_right:
                colour= "green"
            else:
                colour= "red"

            line.append({
                "start":left_points[selected_left],
                "end": right_points[selected_right],
                "colour":colour
            })

    pygame.display.update()

pygame.quit()